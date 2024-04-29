#include "/grade/tests/student_uart.h" // Required to compile. Links your code with the grader

volatile int flag = 0;
int student_main() {
    init_UART();

    while (1) {
        if (flag) {
            printf("Starting to Receive a new UART Frame \n");
            flag = 0;
        }
    }
    return 0;
}

/**
 * ASSUME GPIO has already been initialized for you.
 * ASSUME all aspects of the UART except interrupts have been configured for you.
 * ASSUME the register size of IM, RIS, MIS, and ICR are 1 bit.
 * ASSUME these register names have been memory mapped so you can directly assign values to these names.
 * ASSUME the NVIC has been configured for you.
 */
void init_UART() {
    // TODO: Place your code here to enable the Start of Frame Interrupt

    // Binds UART interrupt requests to My_UART_Handler
    IntRegister(INT_UART, My_UART_Handler);
}

/**
 * UART ISR
 * Give your code for the ISR
 */
void My_UART_Handler() {
    // TODO: Check if an Interrupt has really occurred.
    // TODO: Set flag so student_main() knows interrupt occurred.
    // TODO: Clear the Interrupt.
}
