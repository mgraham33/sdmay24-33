// required for bare metal mode
#include "lm3s6965_headers/LM3S6965.h"
#include "io.h"

// Commented because NUM_INPUTS is inserted by generateHeaders()
// #define NUM_INPUTS 3

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
extern void _minmax();

// Use these as placeholders for any variables, just change the 
// variable after #define to what you need. This will be replaced with valid
// addresses by the generateHeaders() call
#define X *((int *) 0)
#define max *((int *) 0)

void c_entry() {
    volatile int *ptr0 = (&X);
    for (int i = 0; i < NUM_INPUTS; i++) {
        scan_uart0("%d", ptr0);
        ptr0++;
    }

    _minmax();

    for (int i = 0; i < NUM_INPUTS; i++) {
        print_uart0("X[%d]=%d\n", i, (int)((&X)[i]));
    }

    print_uart0("minmax=%d\n", (int)max);

    _exit_qemu();   // exits QEMU cleanly
}
