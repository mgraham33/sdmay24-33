#ifndef UART_H_
#define UART_H_
#include <stdio.h>
#include <stdlib.h>
#include "globals.h"

extern void (*interrupts[100])();
void IntRegister(int interrupt, void (*function)());

#endif
