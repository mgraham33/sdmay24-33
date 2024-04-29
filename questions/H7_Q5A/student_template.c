#include "/grade/tests/student_uart.h" // Required to compile. Links your code with the grader

// Initialize UART0
void init_UART() {
    // TODO: Place your code here

    //Binds UART0 interrupt requests to My_UART0_RX_Handler
    IntRegister(INT_UART1, My_UART0_Handler);
    IntMasterEnable();//Globally allows CPU to service interrupts

}
