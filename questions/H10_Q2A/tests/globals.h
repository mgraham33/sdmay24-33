#ifndef GLOBALS_H_
#define GLOBALS_H_

#include <stdio.h>
#include <stdlib.h>

#define REGISTER_COUNT 33

void randomize_registers();
void reuse_originals();
void fill_originals();
void fill_answers();
void fill_tests();
int check_answers(FILE *out);

typedef struct {
    unsigned int original;
    unsigned int answer;
    unsigned int test;
} register_type;

extern register_type registers[REGISTER_COUNT];

extern char *register_names[REGISTER_COUNT];

// SYSCTL
extern unsigned int SYSCTL_RCGCGPIO_R;
extern unsigned int SYSCTL_RCGCTIMER_R;
extern unsigned int SYSCTL_RCGCADC_R;

// GPIO
extern unsigned int GPIO_PORTB_AFSEL_R;
extern unsigned int GPIO_PORTB_PCTL_R;
extern unsigned int GPIO_PORTB_DEN_R;
extern unsigned int GPIO_PORTB_DIR_R;

extern unsigned int GPIO_PORTE_AFSEL_R;
extern unsigned int GPIO_PORTE_PCTL_R;
extern unsigned int GPIO_PORTE_DEN_R;
extern unsigned int GPIO_PORTE_DIR_R;
extern unsigned int GPIO_PORTE_AMSEL_R;
extern unsigned int GPIO_PORTE_ADCCTL_R;

// TIMER1_A_B
extern unsigned int TIMER1_CTL_R;
extern unsigned int TIMER1_CFG_R;
extern unsigned int TIMER1_TAMR_R;
extern unsigned int TIMER1_TBMR_R;
extern unsigned int TIMER1_TAPR_R;
extern unsigned int TIMER1_TBPR_R;
extern unsigned int TIMER1_TBPMR_R;
extern unsigned int TIMER1_TAILR_R;
extern unsigned int TIMER1_TBILR_R;
extern unsigned int TIMER1_TAMATCHR_R;
extern unsigned int TIMER1_TBMATCHR_R;

// ADC0
extern unsigned int ADC0_ADCCC;
extern unsigned int ADC0_ACTSS_R;
extern unsigned int ADC0_EMUX_R;
extern unsigned int ADC0_SSMUX0_R;
extern unsigned int ADC0_SSCTL0_R;

extern unsigned int ADC0_PSSI_R;
extern unsigned int ADC0_RIS_R;
extern unsigned int ADC0_ISC_R;
extern unsigned int ADC0_SSFIFO0_R;

#endif
