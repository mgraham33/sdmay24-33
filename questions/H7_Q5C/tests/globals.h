#ifndef GLOBALS_H_
#define GLOBALS_H_

extern unsigned char IM;
extern unsigned char RIS;
extern unsigned char MIS;
extern unsigned char ICR;

extern unsigned char INT_UART;
extern unsigned char INT_UART0;
extern unsigned char INT_UART1;
extern unsigned char SYSCTL_RCGCGPIO_R;
extern unsigned char GPIO_PORTA_AFSEL_R;
extern unsigned char GPIO_PORTA_PCTL_R;
extern unsigned char GPIO_PORTA_DEN_R;
extern unsigned char GPIO_PORTA_DIR_R;
extern unsigned char SYSCTL_RCGCUART_R;
extern int UART0_CTL_R;
extern unsigned char UART0_IBRD_R;
extern unsigned char UART0_FBRD_R;
extern unsigned char UART0_CC_R;
extern unsigned char UART0_LCRH_R;
extern unsigned char UART0_ICR_R;
extern unsigned char UART0_IM_R;
extern unsigned char NVIC_PRI1_R;
extern unsigned char NVIC_EN0_R;

#endif