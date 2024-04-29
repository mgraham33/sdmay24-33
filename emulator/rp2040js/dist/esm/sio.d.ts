import { RP2040 } from './rp2040.js';
import { Interpolator } from './interpolator.js';
export declare class RPSIO {
    private readonly rp2040;
    gpioValue: number;
    gpioOutputEnable: number;
    qspiGpioValue: number;
    qspiGpioOutputEnable: number;
    divDividend: number;
    divDivisor: number;
    divQuotient: number;
    divRemainder: number;
    divCSR: number;
    spinLock: number;
    interp0: Interpolator;
    interp1: Interpolator;
    constructor(rp2040: RP2040);
    updateHardwareDivider(signed: boolean): void;
    readUint32(offset: number): number;
    writeUint32(offset: number, value: number): void;
}
