"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.RPClocks = void 0;
const peripheral_js_1 = require("./peripheral.js");
const CLK_REF_CTRL = 0x30;
const CLK_REF_SELECTED = 0x38;
const CLK_SYS_CTRL = 0x3c;
const CLK_SYS_SELECTED = 0x44;
class RPClocks extends peripheral_js_1.BasePeripheral {
    constructor(rp2040, name) {
        super(rp2040, name);
        this.refCtrl = 0;
        this.sysCtrl = 0;
    }
    readUint32(offset) {
        switch (offset) {
            case CLK_REF_CTRL:
                return this.refCtrl;
            case CLK_REF_SELECTED:
                return 1 << (this.refCtrl & 0x03);
            case CLK_SYS_CTRL:
                return this.sysCtrl;
            case CLK_SYS_SELECTED:
                return 1 << (this.sysCtrl & 0x01);
        }
        return super.readUint32(offset);
    }
    writeUint32(offset, value) {
        switch (offset) {
            case CLK_REF_CTRL:
                this.refCtrl = value;
                break;
            case CLK_SYS_CTRL:
                this.sysCtrl = value;
                break;
            default:
                super.writeUint32(offset, value);
                break;
        }
    }
}
exports.RPClocks = RPClocks;
