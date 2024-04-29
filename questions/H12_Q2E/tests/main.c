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
extern void _arrays();

// Use these as placeholders for any variables, just change the 
// variable after #define to what you need. This will be replaced with valid
// addresses by the generateHeaders() call
#define A *((int *) 0)
#define ch1 *((int *) 0)
#define pch *((int *) 0)

void c_entry() {
    unsigned char ch1s[NUM_INPUTS];
    unsigned char *ptr0 = ch1s;
    for (int i = 0; i < NUM_INPUTS; i++) {
        scan_uart0("%d", ptr0);
        ptr0++;
    }

    pch = &ch1;

    for (int i = 0; i < NUM_INPUTS; i++) {
        ch1 = ch1s[i] % 0xff;
        _arrays();
        // We use &A here to get the address of the character given by the macro and use that as our array pointer
        print_uart0("%d: A[%d]=%d\n", i, A_ind, (int)((&A)[A_ind]));
    }

    _exit_qemu();   // exits QEMU cleanly
}
