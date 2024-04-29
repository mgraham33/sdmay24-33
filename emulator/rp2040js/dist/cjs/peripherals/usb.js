"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.RPUSBController = void 0;
const irq_js_1 = require("../irq.js");
const peripheral_js_1 = require("./peripheral.js");
const ENDPOINT_COUNT = 16;
// USB DPSRAM Registers
const EP1_IN_CONTROL = 0x8;
const EP0_IN_BUFFER_CONTROL = 0x80;
const EP0_OUT_BUFFER_CONTROL = 0x84;
const EP15_OUT_BUFFER_CONTROL = 0xfc;
// Endpoint Control bits
const USB_CTRL_DOUBLE_BUF = 1 << 30;
const USB_CTRL_INTERRUPT_PER_TRANSFER = 1 << 29;
// Buffer Control bits
const USB_BUF_CTRL_AVAILABLE = 1 << 10;
const USB_BUF_CTRL_FULL = 1 << 15;
const USB_BUF_CTRL_LEN_MASK = 0x3ff;
// Buffer1
const USB_BUF1_SHIFT = 16;
const USB_BUF1_OFFSET = 64;
// USB Peripheral Register
const MAIN_CTRL = 0x40;
const SIE_STATUS = 0x50;
const BUFF_STATUS = 0x58;
const BUFF_CPU_SHOULD_HANDLE = 0x5c;
const USB_MUXING = 0x74;
const INTR = 0x8c;
const INTE = 0x90;
const INTF = 0x94;
const INTS = 0x98;
// MAIN_CTRL bits
const SIM_TIMING = 1 << 31;
const HOST_NDEVICE = 1 << 1;
const CONTROLLER_EN = 1 << 0;
// SIE_STATUS bits
const SIE_DATA_SEQ_ERROR = 1 << 31;
const SIE_ACK_REC = 1 << 30;
const SIE_STALL_REC = 1 << 29;
const SIE_NAK_REC = 1 << 28;
const SIE_RX_TIMEOUT = 1 << 27;
const SIE_RX_OVERFLOW = 1 << 26;
const SIE_BIT_STUFF_ERROR = 1 << 25;
const SIE_CRC_ERROR = 1 << 24;
const SIE_BUS_RESET = 1 << 19;
const SIE_TRANS_COMPLETE = 1 << 18;
const SIE_SETUP_REC = 1 << 17;
const SIE_CONNECTED = 1 << 16;
const SIE_RESUME = 1 << 11;
const SIE_VBUS_OVER_CURR = 1 << 10;
const SIE_SPEED = 1 << 9;
const SIE_SUSPENDED = 1 << 4;
const SIE_LINE_STATE_MASK = 0x3;
const SIE_LINE_STATE_SHIFT = 2;
const SIE_VBUS_DETECTED = 1 << 0;
// USB_MUXING bits
const SOFTCON = 1 << 3;
const TO_DIGITAL_PAD = 1 << 2;
const TO_EXTPHY = 1 << 1;
const TO_PHY = 1 << 0;
// INTR bits
const INTR_BUFF_STATUS = 1 << 4;
// SIE Line states
var SIELineState;
(function (SIELineState) {
    SIELineState[SIELineState["SE0"] = 0] = "SE0";
    SIELineState[SIELineState["J"] = 1] = "J";
    SIELineState[SIELineState["K"] = 2] = "K";
    SIELineState[SIELineState["SE1"] = 3] = "SE1";
})(SIELineState || (SIELineState = {}));
const SIE_WRITECLEAR_MASK = SIE_DATA_SEQ_ERROR |
    SIE_ACK_REC |
    SIE_STALL_REC |
    SIE_NAK_REC |
    SIE_RX_TIMEOUT |
    SIE_RX_OVERFLOW |
    SIE_BIT_STUFF_ERROR |
    SIE_CONNECTED |
    SIE_CRC_ERROR |
    SIE_BUS_RESET |
    SIE_TRANS_COMPLETE |
    SIE_SETUP_REC |
    SIE_RESUME;
class USBEndpointAlarm {
    constructor(alarm) {
        this.alarm = alarm;
        this.buffers = [];
    }
    schedule(buffer, delayNanos) {
        this.buffers.push(buffer);
        this.alarm.schedule(delayNanos);
    }
}
class RPUSBController extends peripheral_js_1.BasePeripheral {
    get intStatus() {
        return (this.intRaw & this.intEnable) | this.intForce;
    }
    constructor(rp2040, name) {
        super(rp2040, name);
        this.mainCtrl = 0;
        this.intRaw = 0;
        this.intEnable = 0;
        this.intForce = 0;
        this.sieStatus = 0;
        this.buffStatus = 0;
        this.readDelayMicroseconds = 10;
        this.writeDelayMicroseconds = 10; // Determined empirically
        const clock = rp2040.clock;
        this.endpointReadAlarms = [];
        this.endpointWriteAlarms = [];
        for (let i = 0; i < ENDPOINT_COUNT; ++i) {
            this.endpointReadAlarms.push(new USBEndpointAlarm(clock.createAlarm(() => {
                const buffer = this.endpointReadAlarms[i].buffers.shift();
                if (buffer) {
                    this.finishRead(i, buffer);
                }
            })));
            this.endpointWriteAlarms.push(new USBEndpointAlarm(clock.createAlarm(() => {
                var _a;
                for (const buffer of this.endpointWriteAlarms[i].buffers) {
                    (_a = this.onEndpointWrite) === null || _a === void 0 ? void 0 : _a.call(this, i, buffer);
                }
                this.endpointWriteAlarms[i].buffers = [];
            })));
        }
        this.resetAlarm = clock.createAlarm(() => {
            this.sieStatus |= SIE_BUS_RESET;
            this.sieStatusUpdated();
        });
    }
    readUint32(offset) {
        switch (offset) {
            case MAIN_CTRL:
                return this.mainCtrl;
            case SIE_STATUS:
                return this.sieStatus;
            case BUFF_STATUS:
                return this.buffStatus;
            case BUFF_CPU_SHOULD_HANDLE:
                return 0;
            case INTR:
                return this.intRaw;
            case INTE:
                return this.intEnable;
            case INTF:
                return this.intForce;
            case INTS:
                return this.intStatus;
        }
        return super.readUint32(offset);
    }
    writeUint32(offset, value) {
        var _a, _b;
        switch (offset) {
            case MAIN_CTRL:
                this.mainCtrl = value & (SIM_TIMING | CONTROLLER_EN | HOST_NDEVICE);
                if (value & CONTROLLER_EN && !(value & HOST_NDEVICE)) {
                    (_a = this.onUSBEnabled) === null || _a === void 0 ? void 0 : _a.call(this);
                }
                break;
            case BUFF_STATUS:
                this.buffStatus &= ~this.rawWriteValue;
                this.buffStatusUpdated();
                break;
            case USB_MUXING:
                // Workaround for busy wait in hw_enumeration_fix_force_ls_j() / hw_enumeration_fix_finish():
                if (value & TO_DIGITAL_PAD && !(value & TO_PHY)) {
                    this.sieStatus |= SIE_CONNECTED;
                }
                break;
            case SIE_STATUS:
                this.sieStatus &= ~(this.rawWriteValue & SIE_WRITECLEAR_MASK);
                if (this.rawWriteValue & SIE_BUS_RESET) {
                    (_b = this.onResetReceived) === null || _b === void 0 ? void 0 : _b.call(this);
                    this.sieStatus &= ~(SIE_LINE_STATE_MASK << SIE_LINE_STATE_SHIFT);
                    this.sieStatus |= (SIELineState.J << SIE_LINE_STATE_SHIFT) | SIE_CONNECTED;
                }
                this.sieStatusUpdated();
                break;
            case INTE:
                this.intEnable = value & 0xfffff;
                this.checkInterrupts();
                break;
            case INTF:
                this.intForce = value & 0xfffff;
                this.checkInterrupts();
                break;
            default:
                super.writeUint32(offset, value);
        }
    }
    readEndpointControlReg(endpoint, out) {
        const controlRegOffset = EP1_IN_CONTROL + 8 * (endpoint - 1) + (out ? 4 : 0);
        return this.rp2040.usbDPRAMView.getUint32(controlRegOffset, true);
    }
    getEndpointBufferOffset(endpoint, out) {
        if (endpoint === 0) {
            return 0x100;
        }
        return this.readEndpointControlReg(endpoint, out) & 0xffc0;
    }
    DPRAMUpdated(offset, value) {
        var _a, _b;
        if (value & USB_BUF_CTRL_AVAILABLE &&
            offset >= EP0_IN_BUFFER_CONTROL &&
            offset <= EP15_OUT_BUFFER_CONTROL) {
            const endpoint = (offset - EP0_IN_BUFFER_CONTROL) >> 3;
            const bufferOut = offset & 4 ? true : false;
            let doubleBuffer = false;
            let interrupt = true;
            if (endpoint != 0) {
                const control = this.readEndpointControlReg(endpoint, bufferOut);
                doubleBuffer = !!(control & USB_CTRL_DOUBLE_BUF);
                interrupt = !!(control & USB_CTRL_INTERRUPT_PER_TRANSFER);
            }
            if (doubleBuffer && (value >> USB_BUF1_SHIFT) & USB_BUF_CTRL_AVAILABLE) {
                const bufferLength = (value >> USB_BUF1_SHIFT) & USB_BUF_CTRL_LEN_MASK;
                const bufferOffset = this.getEndpointBufferOffset(endpoint, bufferOut) + USB_BUF1_OFFSET;
                this.debug(`Start USB transfer, endPoint=${endpoint}, direction=${bufferOut ? 'out' : 'in'} buffer=${bufferOffset.toString(16)} length=${bufferLength}`);
                value &= ~(USB_BUF_CTRL_AVAILABLE << USB_BUF1_SHIFT);
                this.rp2040.usbDPRAMView.setUint32(offset, value, true);
                if (bufferOut) {
                    (_a = this.onEndpointRead) === null || _a === void 0 ? void 0 : _a.call(this, endpoint, bufferLength);
                }
                else {
                    value &= ~(USB_BUF_CTRL_FULL << USB_BUF1_SHIFT);
                    this.rp2040.usbDPRAMView.setUint32(offset, value, true);
                    const buffer = this.rp2040.usbDPRAM.slice(bufferOffset, bufferOffset + bufferLength);
                    this.indicateBufferReady(endpoint, false);
                    this.endpointWriteAlarms[endpoint].schedule(buffer, this.writeDelayMicroseconds * 1000);
                }
            }
            const bufferLength = value & USB_BUF_CTRL_LEN_MASK;
            const bufferOffset = this.getEndpointBufferOffset(endpoint, bufferOut);
            this.debug(`Start USB transfer, endPoint=${endpoint}, direction=${bufferOut ? 'out' : 'in'} buffer=${bufferOffset.toString(16)} length=${bufferLength}`);
            value &= ~USB_BUF_CTRL_AVAILABLE;
            this.rp2040.usbDPRAMView.setUint32(offset, value, true);
            if (bufferOut) {
                (_b = this.onEndpointRead) === null || _b === void 0 ? void 0 : _b.call(this, endpoint, bufferLength);
            }
            else {
                value &= ~USB_BUF_CTRL_FULL;
                this.rp2040.usbDPRAMView.setUint32(offset, value, true);
                const buffer = this.rp2040.usbDPRAM.slice(bufferOffset, bufferOffset + bufferLength);
                if (interrupt || !doubleBuffer) {
                    this.indicateBufferReady(endpoint, false);
                }
                this.endpointWriteAlarms[endpoint].schedule(buffer, this.writeDelayMicroseconds * 1000);
            }
        }
    }
    endpointReadDone(endpoint, buffer, delay = this.readDelayMicroseconds) {
        this.endpointReadAlarms[endpoint].schedule(buffer, delay * 1000);
    }
    finishRead(endpoint, buffer) {
        const bufferOffset = this.getEndpointBufferOffset(endpoint, true);
        const bufControlReg = EP0_OUT_BUFFER_CONTROL + endpoint * 8;
        let bufControl = this.rp2040.usbDPRAMView.getUint32(bufControlReg, true);
        const requestedLength = bufControl & USB_BUF_CTRL_LEN_MASK;
        const newLength = Math.min(buffer.length, requestedLength);
        bufControl |= USB_BUF_CTRL_FULL;
        bufControl = (bufControl & ~USB_BUF_CTRL_LEN_MASK) | (newLength & USB_BUF_CTRL_LEN_MASK);
        this.rp2040.usbDPRAMView.setUint32(bufControlReg, bufControl, true);
        this.rp2040.usbDPRAM.set(buffer.subarray(0, newLength), bufferOffset);
        this.indicateBufferReady(endpoint, true);
    }
    checkInterrupts() {
        const { intStatus } = this;
        this.rp2040.setInterrupt(irq_js_1.IRQ.USBCTRL, !!intStatus);
    }
    resetDevice() {
        this.resetAlarm.schedule(10000000); // USB reset takes ~10ms
    }
    sendSetupPacket(setupPacket) {
        this.rp2040.usbDPRAM.set(setupPacket);
        this.sieStatus |= SIE_SETUP_REC;
        this.sieStatusUpdated();
    }
    indicateBufferReady(endpoint, out) {
        this.buffStatus |= 1 << (endpoint * 2 + (out ? 1 : 0));
        this.buffStatusUpdated();
    }
    buffStatusUpdated() {
        if (this.buffStatus) {
            this.intRaw |= INTR_BUFF_STATUS;
        }
        else {
            this.intRaw &= ~INTR_BUFF_STATUS;
        }
        this.checkInterrupts();
    }
    sieStatusUpdated() {
        const intRegisterMap = [
            [SIE_SETUP_REC, 1 << 16],
            [SIE_RESUME, 1 << 15],
            [SIE_SUSPENDED, 1 << 14],
            [SIE_CONNECTED, 1 << 13],
            [SIE_BUS_RESET, 1 << 12],
            [SIE_VBUS_DETECTED, 1 << 11],
            [SIE_STALL_REC, 1 << 10],
            [SIE_CRC_ERROR, 1 << 9],
            [SIE_BIT_STUFF_ERROR, 1 << 8],
            [SIE_RX_OVERFLOW, 1 << 7],
            [SIE_RX_TIMEOUT, 1 << 6],
            [SIE_DATA_SEQ_ERROR, 1 << 5],
        ];
        for (const [sieBit, intRawBit] of intRegisterMap) {
            if (this.sieStatus & sieBit) {
                this.intRaw |= intRawBit;
            }
            else {
                this.intRaw &= ~intRawBit;
            }
        }
        this.checkInterrupts();
    }
}
exports.RPUSBController = RPUSBController;
