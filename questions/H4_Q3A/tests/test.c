#include "test.h"

#define TRUE 1
#define FALSE 0

/**
 * For ch
 * Check if ANY of bits {{params.q1a}} are SET to 1
 */
int q1(unsigned char ch) {
    if (TODO1) {
        return TRUE;
    }
    return FALSE;
}

/**
 * For n
 * SET bits {{params.q1bset}} to 1
 * CLEAR bits {{params.q1bclear}} to 0
 * TOGGLE bits {{params.q1btoggle}}
 * and preserve the remaining bits.
 */
unsigned short q2(unsigned short n) {
    return TODO2;
}

/**
 * For n, check
 * If ALL bits {{params.q1callset}} are SET to 1
 * If ALL bits {{params.q1callclear}} are CLEARED to 0
 * If ANY bits {{params.q1canyset}} are SET to 1
 * If ANY bits {{params.q1canyclear}} are CLEARED to 0
 */
int q3(unsigned short n) {
    if (TODO3) {
        return TRUE;
    }
    return FALSE;
}

/**
 * For ch
 * ROTATE all bits to the right {{params.q1d}}.
 * This is also known as a right-barrel-shift operation.
 */
unsigned char q4(unsigned char ch) {
    return (TODO4);
}
