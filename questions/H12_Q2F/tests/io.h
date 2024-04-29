#ifndef __IO_H_
#define __IO_H_

#include "lm3s6965_headers/LM3S6965.h"
#include <stdarg.h>

void print_uart0(const char *format, ...);
void scan_uart0(const char *format, ...);

#endif