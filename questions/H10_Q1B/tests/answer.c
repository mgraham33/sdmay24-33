#include "answer.h"

void answer_init_TIMER1_A_B() {
    SYSCTL_RCGCGPIO_R |= 0x2;

    GPIO_PORTB_AFSEL_R |= 0x30;
    GPIO_PORTB_PCTL_R |= 0x770000;

    GPIO_PORTB_DEN_R |= 0x30;
    GPIO_PORTB_DIR_R |= 0x30;

    SYSCTL_RCGCTIMER_R |= 0x2;

    TIMER1_CTL_R &= ~0x101;

    wait_timer_disable();

    TIMER1_CFG_R = 0x4;
    TIMER1_TAMR_R = 0xa;
    TIMER1_TBMR_R = 0xa;

    TIMER1_CTL_R = 0x0;

    TIMER1_TAPR_R = 0x0;
    TIMER1_TBPR_R = 0x0;

    TIMER1_TAILR_R = 16000;
    TIMER1_TBILR_R = 16000;
    TIMER1_TAMATCHR_R = 8000;
    TIMER1_TBMATCHR_R = 8000;

    TIMER1_CTL_R |= 0x101;
}

void answer_init_ADC() {
    SYSCTL_RCGCGPIO_R |= 0x10;
    GPIO_PORTE_AFSEL_R |= 0x14;

    GPIO_PORTE_DEN_R &= ~0x14;
    GPIO_PORTE_DIR_R &= ~0x14;
    GPIO_PORTE_AMSEL_R |= 0x14;
    GPIO_PORTE_ADCCTL_R &= ~0x18;

    SYSCTL_RCGCADC_R |= 0x1;
    ADC0_ADCCC = 0x0;

    ADC0_ACTSS_R &= ~0x1;

    wait_adc_disable();

    ADC0_EMUX_R &= ~0xf;
    ADC0_SSMUX0_R = 0x0;
    ADC0_SSMUX0_R |= 0x91;

    ADC0_SSCTL0_R = 0x0;
    ADC0_SSCTL0_R |= 0x60;

    ADC0_ACTSS_R |= 0x1;
}

void answer_get_sensor_reading(int *left_sensor, int *right_sensor) {
    ADC0_PSSI_R = 0x1;

    while (~ADC0_RIS_R & 0x1) {
        wait_adc();
    }

    ADC0_ISC_R = 0x1;

    *left_sensor = ADC0_SSFIFO0_R;
    *right_sensor = ADC0_SSFIFO0_R;
}

void answer_set_motor_speed(int left_motor, int right_motor) {
    TIMER1_TAMATCHR_R = 16000 - (16000 * left_motor) / 100;
    TIMER1_TBMATCHR_R = 16000 - (16000 * right_motor) / 100;
}

void answer_compute_motor_values(int left_sensor, int right_sensor, int *left_motor, int *right_motor) {
    int total_sensor = left_sensor + right_sensor;
    *left_motor = (100 * left_sensor) / total_sensor;
    *right_motor = (100 * right_sensor) / total_sensor;
}
