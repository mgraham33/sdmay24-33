#ifndef UTILS_H_
#define UTILS_H_

#include "globals.h"

void wait_adc();
void wait_adc_disable();
void wait_timer_disable();

int getADCWaitCount();
int getADCDisable();
int getTimerDisable();
void resetCounters(int waitCount);

#endif
