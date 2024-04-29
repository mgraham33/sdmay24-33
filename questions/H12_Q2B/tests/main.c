// required for bare metal mode
#include "lm3s6965_headers/LM3S6965.h"
#include "io.h"

#define NUM_INPUTS 5

// functions inserted here

// replaced by generateHeaders()
#define RAND_SIZE 1
// replaced by generateHeaders()
int RAND_ARRAY[RAND_SIZE];

int RAND_PTR = 0;
int rand() {
    if (RAND_PTR >= RAND_SIZE) {
        RAND_PTR = 0;
    }
    return RAND_ARRAY[RAND_PTR++];
}

extern void _exit_qemu();
extern void _logic();

// Use these as placeholders for any variables, just change the 
// variable after #define to what you need. This will be replaced with valid
// addresses by the generateHeaders() call
#define ch1 *((int *) 0)
#define ch2 *((int *) 0)

void c_entry() {
    int ch1s[NUM_INPUTS];
    int ch2s[NUM_INPUTS];
    int *ptr0 = ch1s;
    int *ptr1 = ch2s;
    for (int i = 0; i < NUM_INPUTS; i++) {
        scan_uart0("%d", ptr0);
        scan_uart0("%d", ptr1);
        ptr0++;
        ptr1++;
    }

    for (int i = 0; i < NUM_INPUTS; i++) {
        ch1 = ch1s[i] % 0xff;
        ch2 = ch2s[i] % 0xff;
        _logic();
        print_uart0("%d: ch1=%d ch2=%d\n", i, (int)ch1, (int)ch2);
    }

    _exit_qemu();   // exits QEMU cleanly
}
