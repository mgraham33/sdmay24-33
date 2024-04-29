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

#include "student_software.h"
#include "answer_software_send.h"

int checkAFSEL = 1;

void test_init(FILE *stdout, int pin) {
    int i;
    for (i = 0; i < 100; i++) {
        SYSCTL_RCGCGPIO_R = (unsigned char) rand();
        GPIO_PORTB_DEN_R = (unsigned char) rand();
        GPIO_PORTB_DIR_R = (unsigned char) rand();
        GPIO_PORTB_AFSEL_R = (unsigned char) rand();

        unsigned char mask = 1 << pin;

        unsigned char ans_RCGCGPIO = SYSCTL_RCGCGPIO_R | 0x2;
        unsigned char ans_DEN = GPIO_PORTB_DEN_R | mask;
        unsigned char ans_DIR = GPIO_PORTB_DIR_R | mask;
        unsigned char ans_AFSEL = GPIO_PORTB_AFSEL_R & ~mask;

        init_portB();

        if (SYSCTL_RCGCGPIO_R != ans_RCGCGPIO) {
            fprintf(stdout, "INIT FAILED! SYSCTL_RCGCGPIO_R: %d; EXPECTED: %d\n", SYSCTL_RCGCGPIO_R, ans_RCGCGPIO);
            return;
        }

        if (GPIO_PORTB_DEN_R != ans_DEN) {
            fprintf(stdout, "INIT FAILED! GPIO_PORTB_DEN_R: %d; EXPECTED: %d\n", GPIO_PORTB_DEN_R, ans_DEN);
            return;
        }

        if (GPIO_PORTB_DIR_R != ans_DIR) {
            fprintf(stdout, "INIT FAILED! GPIO_PORTB_DIR_R: %d; EXPECTED: %d\n", GPIO_PORTB_DIR_R, ans_DIR);
            return;
        }

        if (checkAFSEL && GPIO_PORTB_AFSEL_R != ans_AFSEL) {
            fprintf(stdout, "OPTIONAL! GPIO_PORTB_AFSEL_R: %d; EXPECTED: %d\n", GPIO_PORTB_AFSEL_R, ans_AFSEL);
            checkAFSEL = 0;
        }
    }

    fprintf(stdout, "INIT SUCCESS!\n");
}

void test_send(FILE *stdout, int pin) {
    FILE *outfile;
    FILE *answerfile;
    char *filename;

    unsigned long us_temp;
    float us;
    unsigned char data;
    unsigned long us_temp_ans;
    float us_ans;
    unsigned char data_ans;

    int pinmask = 1 << pin;

    unsigned int tempgpio;
    char testcase;
    for (int i = 0; i < 100; i++) {
        tempgpio = (unsigned int)(rand() & 0xffffffff);
        testcase = (char)(rand() & 0xff);

        GPIO_PORTB_DATA_R = tempgpio;
        answerfile = fopen(ANSWERS_FILE, "w");
        if (!answerfile) {
            fprintf(stdout, "Error opening answerfile\n");
            return;
        }
        answer_send(answerfile, testcase, pinmask);
        fclose(answerfile);

        outfile = fopen(OUTPUTS_FILE, "w");
        if (!outfile) {
            fprintf(stdout, "Error opening answerfile\n");
            return;
        }
        fclose(outfile);
        GPIO_PORTB_DATA_R = tempgpio;
        serial_send(testcase);

        outfile = fopen(OUTPUTS_FILE, "r");
        if (!outfile) {
            fprintf(stdout, "Error opening outfile\n");
            return;
        }
        answerfile = fopen(ANSWERS_FILE, "r");
        if (!answerfile) {
            fprintf(stdout, "Error opening answerfile\n");
            return;
        }

        int startfound = 0;
        int datafound = 0;
        int parityfound = 0;
        int stop = 0;
        while(1) {
            int outfstatus = fscanf(outfile, "%ld %hhd", &us_temp, &data);
            us = longtofloat(us_temp);
            int ansfstatus = fscanf(answerfile, "%ld %hhd", &us_temp_ans, &data_ans);
            us_ans = longtofloat(us_temp_ans);
            
            if (outfstatus != 2 && ansfstatus != 2) break;

            if ((outfstatus != 2 || ansfstatus != 2) && !stop) {
                fprintf(stdout, "SEND '%d' FAILED!\n", testcase);
                fclose(outfile);
                fclose(answerfile);
                return;
            }
            else if (!startfound) {
                if (data != data_ans || fabs(us - us_ans) > 0.001) {
                    fprintf(stdout, "SEND '%d' FAILED!\nSTART BIT NOT SENT!\n", testcase);
                    fclose(outfile);
                    fclose(answerfile);
                    return;
                }
                startfound = 1;
            }
            else if (datafound < 8) {
                if (data != data_ans || fabs(us - us_ans) > 0.001) {
                    fprintf(stdout, "SEND '%d' FAILED!\nINCORRECT DATA '%d'; EXPECTED '%d'\n", testcase, data, data_ans);
                    fclose(outfile);
                    fclose(answerfile);
                    return;
                }
                datafound++;
            }
            else if (!parityfound) {
                if (data != data_ans || fabs(us - us_ans) > 0.001) {
                    fprintf(stdout, "SEND '%d' FAILED!\nPARITY BIT NOT SENT!\n", testcase);
                    fclose(outfile);
                    fclose(answerfile);
                    return;
                }
                parityfound = 1;
            }
            else if (stop == 0) {
                if (data == data_ans) {
                    if (fabs(us - us_ans) < 0.001) {
                        stop = 2;
                        continue;
                    }
                    if (fabs(us - (us_ans / 2)) < 0.001) {
                        stop = 1;
                        continue;
                    }
                    fprintf(stdout, "SEND '%d' FAILED!\nSTOP BITS NOT SENT!\n", testcase);
                    fclose(outfile);
                    fclose(answerfile);
                    return;
                }
            }
            else if (stop == 1) {
                if (fabs(us - 104.17) < 0.001) {
                    stop = 2;
                    continue;
                }
                fprintf(stdout, "SEND '%d' FAILED!\nSTOP BITS NOT SENT!\n", testcase);
                fclose(outfile);
                fclose(answerfile);
                return;
            }
            else if (stop == 2) {
                fprintf(stdout, "SEND '%d' FAILED!\nDATA SENT AFTER STOP!\n", testcase);
                fclose(outfile);
                fclose(answerfile);
                return;
            }
        }
        fclose(outfile);
        fclose(answerfile);
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

    int test;
    int pin;

    scanf("%d", &test);
    scanf("%d", &pin);
    switch(test) {
        case 1: { // Test question 1
            test_init(realStdout, pin);
            break;
        }
        case 2: { // Test question 2
            test_send(realStdout, pin);
            break;
        }
    }

    if (errno) {
        fprintf(realStdout, "ERRNO: %d\n", errno);
    }
    return 0;
}
