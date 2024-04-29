"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.u32 = exports.s32 = exports.bit = void 0;
function bit(n) {
    return 1 << n;
}
exports.bit = bit;
function s32(n) {
    return n | 0;
}
exports.s32 = s32;
function u32(n) {
    return n >>> 0;
}
exports.u32 = u32;
