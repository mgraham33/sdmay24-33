#ifndef GLOBALS_H_
#define GLOBALS_H_

// Used for both
extern unsigned char SYSCTL_RCGCGPIO_R;

// Used for software UART
extern unsigned char GPIO_PORTB_DEN_R;
extern unsigned char GPIO_PORTB_DIR_R;
extern unsigned char GPIO_PORTB_AFSEL_R;

extern unsigned char GPIO_PORTB_DATA_R;

// Used for hardware UART
extern unsigned char GPIO_PORTA_AFSEL_R;
extern unsigned long GPIO_PORTA_PCTL_R;
extern unsigned char GPIO_PORTA_DEN_R;
extern unsigned char GPIO_PORTA_DIR_R;

extern unsigned char SYSCTL_RCGCUART_R;
extern unsigned short UART0_CTL_R;
extern unsigned int UART0_IBRD_R;
extern unsigned int UART0_FBRD_R;
extern unsigned int UART0_CC_R;
extern unsigned char UART0_LCRH_R; 

extern unsigned char UART0_FR_R;
extern unsigned char UART0_DR_R;


extern const char* ANSWERS_FILE;
extern const char* INPUTS_FILE;
extern const char* OUTPUTS_FILE;

#endif