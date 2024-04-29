#include "io.h"

void set_uart0(int input) {
    while (UART0->FR & 0x8); // wait for it to stop being busy
    while (~UART0->FR & 0x10);
    UART0->DR = input;
    // for (int i = 0; i < 300; i++) {} // busy loop to let the char through
}

int read_uart0() {
    while (UART0->FR & 0x8); // wait for it to stop being busy
    if (UART0->FR & 0x10) {
        return 0;
    }
    int ret = UART0->DR;
    if (UART0->RSR & 0xff) {
        UART0->RSR &= ~0xff;
        return -1;
    }
    return ret;
}

void print_uart0(const char *format, ...) {
    va_list va;
    va_start(va, format);

    for (int i = 0; format[i] != '\0'; i++) {
        if (format[i] == '%') {
            switch (format[i+1]) {
                case '%': {
                    set_uart0('%');
                    break;
                }
                case 'd': {
                    char msg[20];
                    int in = va_arg(va, int);
                    char *ptr = &msg[19];
                    do {
                        *(--ptr) = (in % 10) + 48;
                        in /= 10;
                    } while (in != 0);
                    while (*ptr != 0) {
                        set_uart0(*ptr++);
                    }
                    break;
                }
                case 'c': {
                    set_uart0(va_arg(va, int));
                    break;
                }
                case 's': {
                    char *ptr = va_arg(va, char*);
                    while (*ptr != '\0') {
                        set_uart0(*ptr++);
                    }
                    break;
                }
            }
            i++;
        } else {
            set_uart0(format[i]);
        }
    }
    va_end(va);
}

void scan_uart0(const char *format, ...) {
    char token[50];
    int k = 0;

    va_list va;
    va_start(va, format);

    for (int i = 0; format[i] != '\0'; i++) {
        token[k++] = format[i];
        if (format[i+1] == '%' || format[i+1] == '\0') {
            token[k] = '\0';
            k = 0;

            char ch1 = token[1];
            if (ch1 == 'i' || ch1 == 'd' || ch1 == 'u') {
                int *input = va_arg(va, int*);
                int read;
                while ((read = read_uart0()) > 47 && read < 58) {
                    *input = (*input * 10) + read - 48;
                }
            } else if (ch1 == 'c') {
                *va_arg(va, char*) = read_uart0();
            } else if (ch1 == 's') {
                char *input = va_arg(va, char*);
                char read;
                while ((read = read_uart0()) != '\0' && read != '\n') {
                    *input = read;
                    input++;
                }
                input = '\0';
            }
        }
    }
    va_end(va);
}
