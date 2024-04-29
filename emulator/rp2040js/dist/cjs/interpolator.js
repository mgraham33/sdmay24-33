"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Interpolator = exports.InterpolatorConfig = void 0;
const bit_js_1 = require("./utils/bit.js");
class InterpolatorConfig {
    constructor(value) {
        this.shift = 0;
        this.maskLSB = 0;
        this.maskMSB = 0;
        this.signed = false;
        this.crossInput = false;
        this.crossResult = false;
        this.addRaw = false;
        this.forceMSB = 0;
        this.blend = false;
        this.clamp = false;
        this.overf0 = false;
        this.overf1 = false;
        this.overf = false;
        this.shift = (value >>> 0) & 0b11111;
        this.maskLSB = (value >>> 5) & 0b11111;
        this.maskMSB = (value >>> 10) & 0b11111;
        this.signed = Boolean((value >>> 15) & 1);
        this.crossInput = Boolean((value >>> 16) & 1);
        this.crossResult = Boolean((value >>> 17) & 1);
        this.addRaw = Boolean((value >>> 18) & 1);
        this.forceMSB = (value >>> 19) & 0b11;
        this.blend = Boolean((value >>> 21) & 1);
        this.clamp = Boolean((value >>> 22) & 1);
        this.overf0 = Boolean((value >>> 23) & 1);
        this.overf1 = Boolean((value >>> 24) & 1);
        this.overf = Boolean((value >>> 25) & 1);
    }
    toUint32() {
        return (((this.shift & 0b11111) << 0) |
            ((this.maskLSB & 0b11111) << 5) |
            ((this.maskMSB & 0b11111) << 10) |
            ((Number(this.signed) & 1) << 15) |
            ((Number(this.crossInput) & 1) << 16) |
            ((Number(this.crossResult) & 1) << 17) |
            ((Number(this.addRaw) & 1) << 18) |
            ((this.forceMSB & 0b11) << 19) |
            ((Number(this.blend) & 1) << 21) |
            ((Number(this.clamp) & 1) << 22) |
            ((Number(this.overf0) & 1) << 23) |
            ((Number(this.overf1) & 1) << 24) |
            ((Number(this.overf) & 1) << 25));
    }
}
exports.InterpolatorConfig = InterpolatorConfig;
class Interpolator {
    constructor(index) {
        this.index = index;
        this.accum0 = 0;
        this.accum1 = 0;
        this.base0 = 0;
        this.base1 = 0;
        this.base2 = 0;
        this.ctrl0 = 0;
        this.ctrl1 = 0;
        this.result0 = 0;
        this.result1 = 0;
        this.result2 = 0;
        this.smresult0 = 0;
        this.smresult1 = 0;
        this.update();
    }
    update() {
        const N = this.index;
        const ctrl0 = new InterpolatorConfig(this.ctrl0);
        const ctrl1 = new InterpolatorConfig(this.ctrl1);
        const do_clamp = ctrl0.clamp && N == 1;
        const do_blend = ctrl0.blend && N == 0;
        ctrl0.clamp = do_clamp;
        ctrl0.blend = do_blend;
        ctrl1.clamp = false;
        ctrl1.blend = false;
        ctrl1.overf0 = false;
        ctrl1.overf1 = false;
        ctrl1.overf = false;
        const input0 = (0, bit_js_1.s32)(ctrl0.crossInput ? this.accum1 : this.accum0);
        const input1 = (0, bit_js_1.s32)(ctrl1.crossInput ? this.accum0 : this.accum1);
        const msbmask0 = ctrl0.maskMSB == 31 ? 0xffffffff : (1 << (ctrl0.maskMSB + 1)) - 1;
        const msbmask1 = ctrl1.maskMSB == 31 ? 0xffffffff : (1 << (ctrl1.maskMSB + 1)) - 1;
        const mask0 = msbmask0 & ~((1 << ctrl0.maskLSB) - 1);
        const mask1 = msbmask1 & ~((1 << ctrl1.maskLSB) - 1);
        const uresult0 = (input0 >>> ctrl0.shift) & mask0;
        const uresult1 = (input1 >>> ctrl1.shift) & mask1;
        const overf0 = Boolean((input0 >>> ctrl0.shift) & ~msbmask0);
        const overf1 = Boolean((input1 >>> ctrl1.shift) & ~msbmask1);
        const overf = overf0 || overf1;
        const sextmask0 = uresult0 & (1 << ctrl0.maskMSB) ? -1 << ctrl0.maskMSB : 0;
        const sextmask1 = uresult1 & (1 << ctrl1.maskMSB) ? -1 << ctrl1.maskMSB : 0;
        const sresult0 = uresult0 | sextmask0;
        const sresult1 = uresult1 | sextmask1;
        const result0 = ctrl0.signed ? sresult0 : uresult0;
        const result1 = ctrl1.signed ? sresult1 : uresult1;
        const addresult0 = this.base0 + (ctrl0.addRaw ? input0 : result0);
        const addresult1 = this.base1 + (ctrl1.addRaw ? input1 : result1);
        const addresult2 = this.base2 + result0 + (do_blend ? 0 : result1);
        const uclamp0 = (0, bit_js_1.u32)(result0) < (0, bit_js_1.u32)(this.base0)
            ? this.base0
            : (0, bit_js_1.u32)(result0) > (0, bit_js_1.u32)(this.base1)
                ? this.base1
                : result0;
        const sclamp0 = (0, bit_js_1.s32)(result0) < (0, bit_js_1.s32)(this.base0)
            ? this.base0
            : (0, bit_js_1.s32)(result0) > (0, bit_js_1.s32)(this.base1)
                ? this.base1
                : result0;
        const clamp0 = ctrl0.signed ? sclamp0 : uclamp0;
        const alpha1 = result1 & 0xff;
        const ublend1 = (0, bit_js_1.u32)(this.base0) + (Math.floor((alpha1 * ((0, bit_js_1.u32)(this.base1) - (0, bit_js_1.u32)(this.base0))) / 256) | 0);
        const sblend1 = (0, bit_js_1.s32)(this.base0) + (Math.floor((alpha1 * ((0, bit_js_1.s32)(this.base1) - (0, bit_js_1.s32)(this.base0))) / 256) | 0);
        const blend1 = ctrl1.signed ? sblend1 : ublend1;
        this.smresult0 = (0, bit_js_1.u32)(result0);
        this.smresult1 = (0, bit_js_1.u32)(result1);
        this.result0 = (0, bit_js_1.u32)(do_blend ? alpha1 : (do_clamp ? clamp0 : addresult0) | (ctrl0.forceMSB << 28));
        this.result1 = (0, bit_js_1.u32)((do_blend ? blend1 : addresult1) | (ctrl0.forceMSB << 28));
        this.result2 = (0, bit_js_1.u32)(addresult2);
        ctrl0.overf0 = overf0;
        ctrl0.overf1 = overf1;
        ctrl0.overf = overf;
        this.ctrl0 = ctrl0.toUint32();
        this.ctrl1 = ctrl1.toUint32();
    }
    writeback() {
        const ctrl0 = new InterpolatorConfig(this.ctrl0);
        const ctrl1 = new InterpolatorConfig(this.ctrl1);
        this.accum0 = (0, bit_js_1.u32)(ctrl0.crossResult ? this.result1 : this.result0);
        this.accum1 = (0, bit_js_1.u32)(ctrl1.crossResult ? this.result0 : this.result1);
        this.update();
    }
    setBase01(value) {
        const N = this.index;
        const ctrl0 = new InterpolatorConfig(this.ctrl0);
        const ctrl1 = new InterpolatorConfig(this.ctrl1);
        const do_blend = ctrl0.blend && N == 0;
        const input0 = value & 0xffff;
        const input1 = (value >>> 16) & 0xffff;
        const sextmask0 = input0 & (1 << 15) ? -1 << 15 : 0;
        const sextmask1 = input1 & (1 << 15) ? -1 << 15 : 0;
        const base0 = (do_blend ? ctrl1.signed : ctrl0.signed) ? input0 | sextmask0 : input0;
        const base1 = ctrl1.signed ? input1 | sextmask1 : input1;
        this.base0 = (0, bit_js_1.u32)(base0);
        this.base1 = (0, bit_js_1.u32)(base1);
        this.update();
    }
}
exports.Interpolator = Interpolator;
