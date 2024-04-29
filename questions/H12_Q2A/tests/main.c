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
extern void _arithmetic();

// Use these as placeholders for any variables, just change the 
// variable after #define to what you need. This will be replaced with valid
// addresses by the generateHeaders() call
#define a *((int *) 0)
#define b *((int *) 0)

void c_entry() {
    int as[NUM_INPUTS];
    int bs[NUM_INPUTS];
    int *aptr = as;
    int *bptr = bs;
    for (int i = 0; i < NUM_INPUTS; i++) {
        scan_uart0("%d", aptr);
        scan_uart0("%d", bptr);
        aptr++;
        bptr++;
    }

    for (int i = 0; i < NUM_INPUTS; i++) {
        a = as[i];
        b = bs[i];
        _arithmetic();
        print_uart0("%d: a=%d b=%d\n", i, a, b);
    }
    
    _exit_qemu();   // exits QEMU cleanly
}
