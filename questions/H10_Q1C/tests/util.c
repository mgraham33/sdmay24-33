#include "util.h"

int adcWaitCount = 0;
void wait_adc() {
    adcWaitCount--;
    if (adcWaitCount <= 0) {
        ADC0_RIS_R |= 0x1;
    }
}

int adcDisable = 0;
void wait_adc_disable() {
    adcDisable = ADC0_ACTSS_R == (registers[24].original & ~0x1);
}

int timerDisable = 0;
void wait_timer_disable() {
    timerDisable = TIMER1_CTL_R == (registers[13].original & ~0x101);
}

int getADCWaitCount() {
    return adcWaitCount;
}

int getADCDisable() {
    return adcDisable;
}

int getTimerDisable() {
    return timerDisable;
}

void resetCounters(int waitCount) {
    adcWaitCount = waitCount;
    adcDisable = 0;
    timerDisable = 0;
}
