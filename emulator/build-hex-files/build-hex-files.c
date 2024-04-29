#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/uart.h"
#include "pico/uartmap288.h"


int main() {

    UART0_DR_R = 'H';
    UART0_DR_R = 'e';
    UART0_DR_R = 'l';
    UART0_DR_R = 'l';
    UART0_DR_R = 'o';
    UART0_DR_R = ',';
    UART0_DR_R = ' ';
    UART0_DR_R = 'W';
    UART0_DR_R = 'o';
    UART0_DR_R = 'r';
    UART0_DR_R = 'l';
    UART0_DR_R = 'd';
    UART0_DR_R = '!';
}