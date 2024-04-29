#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <math.h>
#include <errno.h>
#include <string.h>

#include "student_hardware.h"

void test_init(FILE *stdout, unsigned int lcrh, unsigned int mask, int ibrd, int fbrd) {
    unsigned short ans_CTL = 0x0101;
    unsigned int ans_IBRD = ibrd;
    unsigned int ans_FBRD = fbrd;
    unsigned int ans_CC = 0;
    unsigned char ans_LCRH = lcrh;

    int i;
    for (i = 0; i < 100; i++) {
        SYSCTL_RCGCGPIO_R = (unsigned char) rand();
        GPIO_PORTA_AFSEL_R = (unsigned char) rand();
        GPIO_PORTA_PCTL_R = (((unsigned long) rand()) << 32) | (unsigned long) rand();
        GPIO_PORTA_DEN_R = (unsigned char) rand();
        GPIO_PORTA_DIR_R = (unsigned char) rand();

        SYSCTL_RCGCUART_R = (unsigned char) rand();
        UART0_CTL_R = (unsigned short) rand();
        UART0_IBRD_R = (unsigned int) rand();
        UART0_FBRD_R = (unsigned int) rand();
        UART0_CC_R = (unsigned int) rand();
        UART0_LCRH_R = (unsigned char) rand();

        unsigned char ans_RCGCGPIO = SYSCTL_RCGCGPIO_R | 0x1;
        unsigned char ans_DEN = GPIO_PORTA_DEN_R | 0x2;
        unsigned char ans_DIR = GPIO_PORTA_DIR_R | 0x2;
        unsigned char ans_AFSEL = GPIO_PORTA_AFSEL_R | 0x2;
        unsigned long ans_PCTL = GPIO_PORTA_PCTL_R | 0x10;

        unsigned char ans_RCGCUART = SYSCTL_RCGCUART_R |= 0x1;
        unsigned char orig_LCRH = UART0_LCRH_R;

        serial_init();

        if (SYSCTL_RCGCGPIO_R != ans_RCGCGPIO) {
            fprintf(stdout, "INIT FAILED!\nSYSCTL_RCGCGPIO_R: 0x%.8X; EXPECTED: 0x%.8X\n", SYSCTL_RCGCGPIO_R, ans_RCGCGPIO);
            return;
        }

        if (GPIO_PORTA_DEN_R != ans_DEN) {
            fprintf(stdout, "INIT FAILED!\nGPIO_PORTA_DEN_R: 0x%.8X; EXPECTED: 0x%.8X\n", GPIO_PORTA_DEN_R, ans_DEN);
            return;
        }

        if (GPIO_PORTA_DIR_R != ans_DIR) {
            fprintf(stdout, "INIT FAILED!\nGPIO_PORTA_DIR_R: 0x%.8X; EXPECTED: 0x%.8X\n", GPIO_PORTA_DIR_R, ans_DIR);
            return;
        }

        if (GPIO_PORTA_AFSEL_R != ans_AFSEL) {
            fprintf(stdout, "INIT FAILED!\nGPIO_PORTA_AFSEL_R: 0x%.8X; EXPECTED: 0x%.8X\n", GPIO_PORTA_AFSEL_R, ans_AFSEL);
            return;
        }

        if (GPIO_PORTA_PCTL_R != ans_PCTL) {
            fprintf(stdout, "INIT FAILED!\nGPIO_PORTA_PCTL_R: 0x%.8lX; EXPECTED: 0x%.8lX\n", GPIO_PORTA_PCTL_R, ans_PCTL);
            return;
        }

        if (SYSCTL_RCGCUART_R != ans_RCGCUART) {
            fprintf(stdout, "INIT FAILED!\nSYSCTL_RCGCUART_R: 0x%.8X; EXPECTED: 0x%.8X\n", SYSCTL_RCGCUART_R, ans_RCGCUART);
            return;
        }

        if (UART0_CTL_R != ans_CTL) {
            fprintf(stdout, "INIT FAILED!\nUART0_CTL_R: 0x%.8X; EXPECTED: 0x%.8X\n", UART0_CTL_R, ans_CTL);
            return;
        }

        if (UART0_IBRD_R != ans_IBRD) {
            fprintf(stdout, "INIT FAILED!\nUART0_IBRD_R: 0x%.8X; EXPECTED: 0x%.8X\n", UART0_IBRD_R, ans_IBRD);
            return;
        }

        if (UART0_FBRD_R != ans_FBRD) {
            fprintf(stdout, "INIT FAILED!\nUART0_FBRD_R: 0x%.8X; EXPECTED: 0x%.8X\n", UART0_FBRD_R, ans_FBRD);
            return;
        }

        if (UART0_CC_R != ans_CC) {
            fprintf(stdout, "INIT FAILED!\nUART0_CC_R: 0x%.8X; EXPECTED: 0x%.8X\n", UART0_CC_R, ans_CC);
            return;
        }

        // Checks if the masked bits are correct according to the answer, and the unmasked bits are the original
        if (((UART0_LCRH_R & mask) != (ans_LCRH & mask)) || ((UART0_LCRH_R & ~mask) != (orig_LCRH & ~mask))) {
            fprintf(stdout, "INIT FAILED!\nUART0_LCRH_R: 0x%.8X; EXPECTED: 0x%.8X\n", UART0_LCRH_R, ans_LCRH);
            return;
        }
    }

    fprintf(stdout, "INIT SUCCESS!\n");
}

void test_send(FILE *stdout) {
    int i;
    for (i = 0; i < 100; i++) {
        unsigned char my_text = (unsigned char) rand();
        UART0_FR_R = (unsigned char) rand();
        UART0_DR_R = (unsigned char) rand();

        unsigned char ans_FR = UART0_FR_R & ~0x20;
        int ans_waited = ans_FR != UART0_FR_R;

        serial_send(my_text);
        
        if (UART0_DR_R != my_text) {
            fprintf(stdout, "SEND FAILED!\nINCORRECT CHARACTER '0x%.2X'; EXPECTED '0x%.2X'\n", UART0_DR_R, my_text);
            return;
        }

        if (UART0_FR_R != ans_FR || hasWaited() != ans_waited) {
            fprintf(stdout, "SEND FAILED!\nINCORRECT WAIT SETUP\n");
            return;
        }
    }

    fprintf(stdout, "SEND SUCCESS!\n");
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

    unsigned int lcrh;
    unsigned int mask;
    int ibrd;
    int fbrd;
    scanf("%d\n", &lcrh);
    scanf("%d\n", &mask);
    scanf("%d\n", &ibrd);
    scanf("%d\n", &fbrd);

    test_init(realStdout, lcrh, mask, ibrd, fbrd);
    test_send(realStdout);

    if (errno) {
        fprintf(realStdout, "ERRNO: %d\n", errno);
    }
    return 0;
}
