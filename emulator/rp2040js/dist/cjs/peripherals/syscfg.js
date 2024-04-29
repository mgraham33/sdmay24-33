"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.RP2040SysCfg = void 0;
const peripheral_js_1 = require("./peripheral.js");
const PROC0_NMI_MASK = 0;
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const PROC1_NMI_MASK = 4;
class RP2040SysCfg extends peripheral_js_1.BasePeripheral {
    readUint32(offset) {
        switch (offset) {
            case PROC0_NMI_MASK:
                return this.rp2040.core.interruptNMIMask;
        }
        return super.readUint32(offset);
    }
    writeUint32(offset, value) {
        switch (offset) {
            case PROC0_NMI_MASK:
                this.rp2040.core.interruptNMIMask = value;
                break;
            default:
                super.writeUint32(offset, value);
        }
    }
}
exports.RP2040SysCfg = RP2040SysCfg;
