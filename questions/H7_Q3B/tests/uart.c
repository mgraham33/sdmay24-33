#include "uart.h"

long floattolong(float f) {
    union {
        float f;
        unsigned long l;
    } temp;
    temp.f = f;
    return temp.l;
}

float longtofloat(unsigned long l) {
    union {
        float f;
        unsigned long l;
    } temp;
    temp.l = l;
    return temp.f;
}

void wait_us(float us) {
    FILE *outfile = fopen(OUTPUTS_FILE, "a");

    fprintf(outfile, "%ld %d\n", floattolong(us), GPIO_PORTB_DATA_R);

    fclose(outfile);
}

int waited = 0;
void wait() {
    UART0_FR_R &= ~0x20;
    waited++;
}

int hasWaited() {
    int wait = waited;
    if (!waited) return 0;
    waited = 0;
    return wait;
}
