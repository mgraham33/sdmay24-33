#ifndef UART_H_
#define UART_H_
#include <stdio.h>
#include <stdlib.h>
#include "globals.h"

long floattolong(float f);
float longtofloat(unsigned long l);
void wait_us(float us);
void wait();
int hasWaited();

#endif
