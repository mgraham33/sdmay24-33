#include "answer.h"

void answer_init_TIMER1(unsigned int period_ms, unsigned int duty) {
    SYSCTL_RCGCTIMER_R |= 0x2;

    TIMER1_CTL_R &= ~0x100;

    wait_timer_disable();

    TIMER1_CFG_R = 0x4;
    TIMER1_TBMR_R = 0xa;

    TIMER1_CTL_R = 0x0;

    int cycles = period_ms * 16000;

    TIMER1_TBPR_R = cycles >> 16;
    TIMER1_TBILR_R = cycles & 0xffff;
    
    cycles = (unsigned int)(cycles * (duty / 100.0f));

    TIMER1_TBPMR_R = cycles >> 16;
    TIMER1_TBMATCHR_R = cycles & 0xffff;

    TIMER1_CTL_R |= 0x100;
}
