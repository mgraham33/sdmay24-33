import { RP2040 } from '../rp2040.js';
import { BasePeripheral, Peripheral } from './peripheral.js';
export declare class RPClocks extends BasePeripheral implements Peripheral {
    refCtrl: number;
    sysCtrl: number;
    constructor(rp2040: RP2040, name: string);
    readUint32(offset: number): number;
    writeUint32(offset: number, value: number): void;
}
