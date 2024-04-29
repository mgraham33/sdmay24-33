#include "uart.h"

void (*interrupts[100])();

void IntRegister(int interrupt, void (*interrupt_func)()) {
    interrupts[interrupt] = interrupt_func;
}
