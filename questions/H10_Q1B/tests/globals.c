#include "globals.h"

register_type registers[REGISTER_COUNT];

char *register_names[REGISTER_COUNT] = {
    "SYSCTL_RCGCGPIO_R",
    "SYSCTL_RCGCTIMER_R",
    "SYSCTL_RCGCADC_R",
    "GPIO_PORTB_AFSEL_R",
    "GPIO_PORTB_PCTL_R",
    "GPIO_PORTB_DEN_R",
    "GPIO_PORTB_DIR_R",
    "GPIO_PORTE_AFSEL_R",
    "GPIO_PORTE_PCTL_R",
    "GPIO_PORTE_DEN_R",
    "GPIO_PORTE_DIR_R",
    "GPIO_PORTE_AMSEL_R",
    "GPIO_PORTE_ADCCTL_R",
    "TIMER1_CTL_R",
    "TIMER1_CFG_R",
    "TIMER1_TAMR_R",
    "TIMER1_TBMR_R",
    "TIMER1_TAPR_R",
    "TIMER1_TBPR_R",
    "TIMER1_TAILR_R",
    "TIMER1_TBILR_R",
    "TIMER1_TAMATCHR_R",
    "TIMER1_TBMATCHR_R",
    "ADC0_ADCCC",
    "ADC0_ACTSS_R",
    "ADC0_EMUX_R",
    "ADC0_SSMUX0_R",
    "ADC0_SSCTL0_R",
    "ADC0_PSSI_R",
    "ADC0_RIS_R",
    "ADC0_ISC_R",
    "ADC0_SSFIFO0_R"
};

// SYSCTL
unsigned int SYSCTL_RCGCGPIO_R;
unsigned int SYSCTL_RCGCTIMER_R;
unsigned int SYSCTL_RCGCADC_R;

// GPIO
unsigned int GPIO_PORTB_AFSEL_R;
unsigned int GPIO_PORTB_PCTL_R;
unsigned int GPIO_PORTB_DEN_R;
unsigned int GPIO_PORTB_DIR_R;

unsigned int GPIO_PORTE_AFSEL_R;
unsigned int GPIO_PORTE_PCTL_R;
unsigned int GPIO_PORTE_DEN_R;
unsigned int GPIO_PORTE_DIR_R;
unsigned int GPIO_PORTE_AMSEL_R;
unsigned int GPIO_PORTE_ADCCTL_R;

// TIMER1_A_B
unsigned int TIMER1_CTL_R;
unsigned int TIMER1_CFG_R;
unsigned int TIMER1_TAMR_R;
unsigned int TIMER1_TBMR_R;
unsigned int TIMER1_TAPR_R;
unsigned int TIMER1_TBPR_R;
unsigned int TIMER1_TAILR_R;
unsigned int TIMER1_TBILR_R;
unsigned int TIMER1_TAMATCHR_R;
unsigned int TIMER1_TBMATCHR_R;

// ADC0
unsigned int ADC0_ADCCC;
unsigned int ADC0_ACTSS_R;
unsigned int ADC0_EMUX_R;
unsigned int ADC0_SSMUX0_R;
unsigned int ADC0_SSCTL0_R;

unsigned int ADC0_PSSI_R;
unsigned int ADC0_RIS_R;
unsigned int ADC0_ISC_R;
unsigned int ADC0_SSFIFO0_R;

void setOptional(int reg, uint8_t optional) {
    registers[reg].optional = optional;
}

void clearOptionals() {
    for (int i = 0; i < REGISTER_COUNT; i++) {
        registers[i].optional = 0;
    }
}

void randomize_registers() {
    // SYSCTL
    SYSCTL_RCGCGPIO_R = (unsigned int) rand();
    SYSCTL_RCGCTIMER_R = (unsigned int) rand();
    SYSCTL_RCGCADC_R = (unsigned int) rand();

    // GPIO
    GPIO_PORTB_AFSEL_R = (unsigned int) rand();
    GPIO_PORTB_PCTL_R = (unsigned int) rand();
    GPIO_PORTB_DEN_R = (unsigned int) rand();
    GPIO_PORTB_DIR_R = (unsigned int) rand();

    GPIO_PORTE_AFSEL_R = (unsigned int) rand();
    GPIO_PORTE_PCTL_R = (unsigned int) rand();
    GPIO_PORTE_DEN_R = (unsigned int) rand();
    GPIO_PORTE_DIR_R = (unsigned int) rand();
    GPIO_PORTE_AMSEL_R = (unsigned int) rand();
    GPIO_PORTE_ADCCTL_R = (unsigned int) rand();

    // TIMER1_A_B
    TIMER1_CTL_R = (unsigned int) rand();
    TIMER1_CFG_R = (unsigned int) rand();
    TIMER1_TAMR_R = (unsigned int) rand();
    TIMER1_TBMR_R = (unsigned int) rand();
    TIMER1_TAPR_R = (unsigned int) rand();
    TIMER1_TBPR_R = (unsigned int) rand();
    TIMER1_TAILR_R = (unsigned int) rand();
    TIMER1_TBILR_R = (unsigned int) rand();
    TIMER1_TAMATCHR_R = (unsigned int) rand();
    TIMER1_TBMATCHR_R = (unsigned int) rand();

    // ADC0
    ADC0_ADCCC = (unsigned int) rand();
    ADC0_ACTSS_R = (unsigned int) rand();
    ADC0_EMUX_R = (unsigned int) rand();
    ADC0_SSMUX0_R = (unsigned int) rand();
    ADC0_SSCTL0_R = (unsigned int) rand();

    ADC0_PSSI_R = (unsigned int) rand();
    ADC0_RIS_R = (unsigned int) rand();
    ADC0_ISC_R = (unsigned int) rand();
    ADC0_SSFIFO0_R = (unsigned int) rand();

    fill_originals();
}

void reuse_originals() {
    // SYSCTL
    SYSCTL_RCGCGPIO_R = registers[0].original;
    SYSCTL_RCGCTIMER_R = registers[1].original;
    SYSCTL_RCGCADC_R = registers[2].original;

    // GPIO
    GPIO_PORTB_AFSEL_R = registers[3].original;
    GPIO_PORTB_PCTL_R = registers[4].original;
    GPIO_PORTB_DEN_R = registers[5].original;
    GPIO_PORTB_DIR_R = registers[6].original;

    GPIO_PORTE_AFSEL_R = registers[7].original;
    GPIO_PORTE_PCTL_R = registers[8].original;
    GPIO_PORTE_DEN_R = registers[9].original;
    GPIO_PORTE_DIR_R = registers[10].original;
    GPIO_PORTE_AMSEL_R = registers[11].original;
    GPIO_PORTE_ADCCTL_R = registers[12].original;

    // TIMER1_A_B
    TIMER1_CTL_R = registers[13].original;
    TIMER1_CFG_R = registers[14].original;
    TIMER1_TAMR_R = registers[15].original;
    TIMER1_TBMR_R = registers[16].original;
    TIMER1_TAPR_R = registers[17].original;
    TIMER1_TBPR_R = registers[18].original;
    TIMER1_TAILR_R = registers[19].original;
    TIMER1_TBILR_R = registers[20].original;
    TIMER1_TAMATCHR_R = registers[21].original;
    TIMER1_TBMATCHR_R = registers[22].original;

    // ADC0
    ADC0_ADCCC = registers[23].original;
    ADC0_ACTSS_R = registers[24].original;
    ADC0_EMUX_R = registers[25].original;
    ADC0_SSMUX0_R = registers[26].original;
    ADC0_SSCTL0_R = registers[27].original;

    ADC0_PSSI_R = registers[28].original;
    ADC0_RIS_R = registers[29].original;
    ADC0_ISC_R = registers[30].original;
    ADC0_SSFIFO0_R = registers[31].original;
}

void fill_originals() {
    // SYSCTL
    registers[0].original = SYSCTL_RCGCGPIO_R;
    registers[1].original = SYSCTL_RCGCTIMER_R;
    registers[2].original = SYSCTL_RCGCADC_R;

    // GPIO
    registers[3].original = GPIO_PORTB_AFSEL_R;
    registers[4].original = GPIO_PORTB_PCTL_R;
    registers[5].original = GPIO_PORTB_DEN_R;
    registers[6].original = GPIO_PORTB_DIR_R;

    registers[7].original = GPIO_PORTE_AFSEL_R;
    registers[8].original = GPIO_PORTE_PCTL_R;
    registers[9].original = GPIO_PORTE_DEN_R;
    registers[10].original = GPIO_PORTE_DIR_R;
    registers[11].original = GPIO_PORTE_AMSEL_R;
    registers[12].original = GPIO_PORTE_ADCCTL_R;

    // TIMER1_A_B
    registers[13].original = TIMER1_CTL_R;
    registers[14].original = TIMER1_CFG_R;
    registers[15].original = TIMER1_TAMR_R;
    registers[16].original = TIMER1_TBMR_R;
    registers[17].original = TIMER1_TAPR_R;
    registers[18].original = TIMER1_TBPR_R;
    registers[19].original = TIMER1_TAILR_R;
    registers[20].original = TIMER1_TBILR_R;
    registers[21].original = TIMER1_TAMATCHR_R;
    registers[22].original = TIMER1_TBMATCHR_R;

    // ADC0
    registers[23].original = ADC0_ADCCC;
    registers[24].original = ADC0_ACTSS_R;
    registers[25].original = ADC0_EMUX_R;
    registers[26].original = ADC0_SSMUX0_R;
    registers[27].original = ADC0_SSCTL0_R;

    registers[28].original = ADC0_PSSI_R;
    registers[29].original = ADC0_RIS_R;
    registers[30].original = ADC0_ISC_R;
    registers[31].original = ADC0_SSFIFO0_R;
}

void fill_answers() {
    // SYSCTL
    registers[0].answer = SYSCTL_RCGCGPIO_R;
    registers[1].answer = SYSCTL_RCGCTIMER_R;
    registers[2].answer = SYSCTL_RCGCADC_R;

    // GPIO
    registers[3].answer = GPIO_PORTB_AFSEL_R;
    registers[4].answer = GPIO_PORTB_PCTL_R;
    registers[5].answer = GPIO_PORTB_DEN_R;
    registers[6].answer = GPIO_PORTB_DIR_R;

    registers[7].answer = GPIO_PORTE_AFSEL_R;
    registers[8].answer = GPIO_PORTE_PCTL_R;
    registers[9].answer = GPIO_PORTE_DEN_R;
    registers[10].answer = GPIO_PORTE_DIR_R;
    registers[11].answer = GPIO_PORTE_AMSEL_R;
    registers[12].answer = GPIO_PORTE_ADCCTL_R;

    // TIMER1_A_B
    registers[13].answer = TIMER1_CTL_R;
    registers[14].answer = TIMER1_CFG_R;
    registers[15].answer = TIMER1_TAMR_R;
    registers[16].answer = TIMER1_TBMR_R;
    registers[17].answer = TIMER1_TAPR_R;
    registers[18].answer = TIMER1_TBPR_R;
    registers[19].answer = TIMER1_TAILR_R;
    registers[20].answer = TIMER1_TBILR_R;
    registers[21].answer = TIMER1_TAMATCHR_R;
    registers[22].answer = TIMER1_TBMATCHR_R;

    // ADC0
    registers[23].answer = ADC0_ADCCC;
    registers[24].answer = ADC0_ACTSS_R;
    registers[25].answer = ADC0_EMUX_R;
    registers[26].answer = ADC0_SSMUX0_R;
    registers[27].answer = ADC0_SSCTL0_R;

    registers[28].answer = ADC0_PSSI_R;
    registers[29].answer = ADC0_RIS_R;
    registers[30].answer = ADC0_ISC_R;
    registers[31].answer = ADC0_SSFIFO0_R;
}

void fill_tests() {
    // SYSCTL
    registers[0].test = SYSCTL_RCGCGPIO_R;
    registers[1].test = SYSCTL_RCGCTIMER_R;
    registers[2].test = SYSCTL_RCGCADC_R;

    // GPIO
    registers[3].test = GPIO_PORTB_AFSEL_R;
    registers[4].test = GPIO_PORTB_PCTL_R;
    registers[5].test = GPIO_PORTB_DEN_R;
    registers[6].test = GPIO_PORTB_DIR_R;

    registers[7].test = GPIO_PORTE_AFSEL_R;
    registers[8].test = GPIO_PORTE_PCTL_R;
    registers[9].test = GPIO_PORTE_DEN_R;
    registers[10].test = GPIO_PORTE_DIR_R;
    registers[11].test = GPIO_PORTE_AMSEL_R;
    registers[12].test = GPIO_PORTE_ADCCTL_R;

    // TIMER1_A_B
    registers[13].test = TIMER1_CTL_R;
    registers[14].test = TIMER1_CFG_R;
    registers[15].test = TIMER1_TAMR_R;
    registers[16].test = TIMER1_TBMR_R;
    registers[17].test = TIMER1_TAPR_R;
    registers[18].test = TIMER1_TBPR_R;
    registers[19].test = TIMER1_TAILR_R;
    registers[20].test = TIMER1_TBILR_R;
    registers[21].test = TIMER1_TAMATCHR_R;
    registers[22].test = TIMER1_TBMATCHR_R;

    // ADC0
    registers[23].test = ADC0_ADCCC;
    registers[24].test = ADC0_ACTSS_R;
    registers[25].test = ADC0_EMUX_R;
    registers[26].test = ADC0_SSMUX0_R;
    registers[27].test = ADC0_SSCTL0_R;

    registers[28].test = ADC0_PSSI_R;
    registers[29].test = ADC0_RIS_R;
    registers[30].test = ADC0_ISC_R;
    registers[31].test = ADC0_SSFIFO0_R;
}

int check_answers(FILE *out) {
    int i;
    for (i = 0; i < REGISTER_COUNT; i++) {
        unsigned int answer = registers[i].answer;
        unsigned int test = registers[i].test;
        unsigned int original = registers[i].original;
        if (test != answer) {
            switch (registers[i].optional) {
                case 0: {
                    fprintf(out, "Error: register '%s' was originally '0x%08X'; it should be '0x%08X' but was set to '0x%08X'.\n", register_names[i],  original, answer, test);
                    return 0;
                }
                case 1: {
                    fprintf(out, "Warning: optional register '%s' was originally '0x%08X'; it should be '0x%08X' but was set to '0x%08X'.\n", register_names[i],  original, answer, test);
                    registers[i].optional = 2;
                }
                default:
            }
        }
    }
    return 1;
}
