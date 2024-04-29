#include "answer_software_send.h"

void write(FILE *answerfile, float BitTime) {
    fprintf(answerfile, "%ld %d\n", floattolong(BitTime), GPIO_PORTB_DATA_R);
}

void answer_send(FILE *file, char my_text, int mask) {
    int i = 0;
    int odd_parity = 1;
    float BitTime = 104.17;
    // Send Start bit
    GPIO_PORTB_DATA_R = GPIO_PORTB_DATA_R & ~mask;
    write(file, BitTime);
    // Send Data bits
    for(i=0; i < 8; i++) {
        if( ((my_text>>i) & 0x01) ) {
            GPIO_PORTB_DATA_R = GPIO_PORTB_DATA_R | mask; //Send 1
        } else {
            GPIO_PORTB_DATA_R = GPIO_PORTB_DATA_R & ~mask; //Send 0
        }
        write(file, BitTime);
    }

    // Compute and send Odd Parity bit
    for(i=0; i < 8; i++) {
        odd_parity = odd_parity ^ ((my_text>>i) & 0x01);
    }

    if(odd_parity) {
        GPIO_PORTB_DATA_R = GPIO_PORTB_DATA_R | mask;
    } else {
        GPIO_PORTB_DATA_R = GPIO_PORTB_DATA_R & ~mask;
    }
    
    write(file, BitTime);
    // Send 2 stop bits
    GPIO_PORTB_DATA_R = GPIO_PORTB_DATA_R | mask;
    write(file, 2*BitTime);
}
