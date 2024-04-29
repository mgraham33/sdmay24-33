#include "main.h"

int done_testing = 0;

void test_main(FILE *stdout) {

    if (SYSCTL_RCGCGPIO_R != 0)
    {
        fprintf(stdout, "INCORRECT SYSCTL_RCGCGPIO_R\nEXPECTED: %d\nACTUAL: %d\n", 0, SYSCTL_RCGCGPIO_R);
        return;
    }
    else if (GPIO_PORTA_AFSEL_R != 0)
    {
        fprintf(stdout, "INCORRECT GPIO_PORTA_AFSEL_R\nEXPECTED: %d\nACTUAL: %d\n", 0, GPIO_PORTA_AFSEL_R);
        return;
    }
    else if (GPIO_PORTA_DEN_R != 0)
    {
        fprintf(stdout, "INCORRECT GPIO_PORTA_DEN_R\nEXPECTED: %d\nACTUAL: %d\n", 0, GPIO_PORTA_DEN_R);
        return;
    }
    else if (GPIO_PORTA_DIR_R != 0)
    {
        fprintf(stdout, "INCORRECT GPIO_PORTA_DIR_R\nEXPECTED: %d\nACTUAL: %d\n", 0, GPIO_PORTA_DIR_R);
        return;
    }
    else if (SYSCTL_RCGCUART_R != 0)
    {
        fprintf(stdout, "INCORRECT SYSCTL_RCGCUART_R\nEXPECTED: %d\nACTUAL: %d\n", 0, SYSCTL_RCGCUART_R);
        return;
    }
    else if (UART0_IBRD_R != 0)
    {
        fprintf(stdout, "INCORRECT UART0_IBRD_R\nEXPECTED: %d\nACTUAL: %d\n", 0, UART0_IBRD_R);
        return;
    }
    else if (UART0_FBRD_R != 0)
    {
        fprintf(stdout, "INCORRECT UART0_FBRD_R\nEXPECTED: %d\nACTUAL: %d\n", 0, UART0_FBRD_R);
        return;
    }
    else if (UART0_CC_R != 0)
    {
        fprintf(stdout, "INCORRECT UART0_CC_R\nEXPECTED: %d\nACTUAL: %d\n", 0, UART0_CC_R);
        return;
    }
    else if (UART0_LCRH_R != 0)
    {
        fprintf(stdout, "INCORRECT UART0_LCRH_R\nEXPECTED: %d\nACTUAL: %d\n", 0, UART0_LCRH_R);
        return;
    }
    else if (UART0_ICR_R != 0)
    {
        fprintf(stdout, "INCORRECT UART0_ICR_R\nEXPECTED: %d\nACTUAL: %d\n", 0, UART0_ICR_R);
        return;
    }
    else if (UART0_IM_R != 0){
        fprintf(stdout, "INCORRECT UART0_IM_R\nEXPECTED: %d\nACTUAL: %d\n", 0, UART0_IM_R);
        return;
    }
    else if (NVIC_PRI1_R != 0){
        fprintf(stdout, "INCORRECT NVIC_PRI1_R\nEXPECTED: %d\nACTUAL: %d\n", 0, NVIC_PRI1_R);
        return;
    }
    else if (NVIC_EN0_R != 0){
        fprintf(stdout, "INCORRECT NVIC_EN0_R\nEXPECTED: %d\nACTUAL: %d\n", 0, NVIC_EN0_R);
        return;
    }
    else if (UART0_CTL_R != 0){
        fprintf(stdout, "INCORRECT UART0_CTL_R\nEXPECTED: %d\nACTUAL: %d\n", 0, UART0_CTL_R);
        return;
    }

    fprintf(stdout, "SUCCESS!\n");
}

void My_UART0_Handler() {

}

void IntMasterEnable() {

}

int main() {
    /* Saves stdout in a new file descriptor */
    int realStdoutNo = dup(STDOUT_FILENO);
    FILE *realStdout = fdopen(realStdoutNo, "w");

    /* Switches stdout/stderr to point to different file descriptor to
    * avoid students passing code by printing the correct result. */
    int devNull = open("/dev/null", O_WRONLY);
    dup2(devNull, STDOUT_FILENO);
    dup2(devNull, STDERR_FILENO);

    test_main(realStdout);

    if (errno) {
        fprintf(realStdout, "Error: %d\n", errno);
    }
    return errno;
}
