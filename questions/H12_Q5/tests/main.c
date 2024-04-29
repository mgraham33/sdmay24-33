// required for bare metal mode
#include "lm3s6965_headers/LM3S6965.h"
#include "io.h"

#define NUM_INPUTS 3

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
extern void _complex_comparison();

// Use these as placeholders for any variables, just change the 
// variable after #define to what you need. This will be replaced with valid
// addresses by the generateHeaders() call
#define a *((int *) 0)
#define b *((int *) 0)
#define c *((int *) 0)
#define d *((int *) 0)
#define flag *((int *) 0)

void c_entry() {
    int as[NUM_INPUTS];
    int bs[NUM_INPUTS];
    int cs[NUM_INPUTS];
    int ds[NUM_INPUTS];
    int *ptr0 = as;
    int *ptr1 = bs;
    int *ptr2 = cs;
    int *ptr3 = ds;
    for (int i = 0; i < NUM_INPUTS; i++) {
        scan_uart0("%d", ptr0);
        scan_uart0("%d", ptr1);
        scan_uart0("%d", ptr2);
        scan_uart0("%d", ptr3);
        ptr0++;
        ptr1++;
        ptr2++;
        ptr3++;
    }

    for (int i = 0; i < NUM_INPUTS; i++) {
        a = as[i] % 0xff;
        b = bs[i] % 0xff;
        c = cs[i] % 0xff;
        d = ds[i] % 0xff;
        flag = 2;
        _complex_comparison();
        print_uart0("%d: flag=%d\n", i, (int)flag);
    }

    _exit_qemu();   // exits QEMU cleanly
}
