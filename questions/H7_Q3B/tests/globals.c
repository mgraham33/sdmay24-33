#include "globals.h"

// Used for both
unsigned char SYSCTL_RCGCGPIO_R = 0;

// Used for software UART
unsigned char GPIO_PORTB_DEN_R = 0;
unsigned char GPIO_PORTB_DIR_R = 0;
unsigned char GPIO_PORTB_AFSEL_R = 0;

unsigned char GPIO_PORTB_DATA_R = 0;

// Used for hardware UART
unsigned char GPIO_PORTA_AFSEL_R = 0;
unsigned long GPIO_PORTA_PCTL_R = 0;
unsigned char GPIO_PORTA_DEN_R = 0;
unsigned char GPIO_PORTA_DIR_R = 0;

unsigned char SYSCTL_RCGCUART_R = 0;
unsigned short UART0_CTL_R = 0;
unsigned int UART0_IBRD_R = 0;
unsigned int UART0_FBRD_R = 0;
unsigned int UART0_CC_R = 0;
unsigned char UART0_LCRH_R = 0; 

unsigned char UART0_FR_R = 0;
unsigned char UART0_DR_R = 0;

const char* ANSWERS_FILE = "send_answers.txt";
const char* INPUTS_FILE = "inputs.txt";
const char* OUTPUTS_FILE = "/grade/tests/send_outputs.txt";