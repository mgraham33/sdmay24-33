#include "main.h"

int done_testing = 0;

void test_main(FILE *stdout) {
    int i;
    int j;
    for (i = 0; i < 100; i++) {
        IM = (unsigned char) rand();
        unsigned char ans_IM = IM | 0x1;
        RIS = (unsigned char) rand();
        unsigned char ans_RIS = RIS;
        MIS = (unsigned char) rand() % 2;
        unsigned char ans_MIS = MIS;
        ICR = (unsigned char) rand();
        unsigned char ans_ICR = MIS ? 1 : ICR;
        int flag_ans = MIS ? 1 : 0;

        for (j = 0; j < 100; j++) {
            interrupts[j] = NULL;
        }
        INT_UART = (unsigned char) (rand() % 100);

        init_UART();
        (*interrupts[INT_UART])();

        if (IM != ans_IM) {
            fprintf(stdout, "INCORRECT IM\nEXPECTED: %d\nACTUAL: %d\n", ans_IM, IM);
            return;
        } else if (RIS != ans_RIS) {
            fprintf(stdout, "INCORRECT RIS\nEXPECTED: %d\nACTUAL: %d\n", ans_RIS, RIS);
            return;
        } else if (MIS != ans_MIS) {
            fprintf(stdout, "INCORRECT MIS\nEXPECTED: %d\nACTUAL: %d\n", ans_MIS, MIS);
            return;
        } else if (ICR != ans_ICR) {
            fprintf(stdout, "INCORRECT ICR\nEXPECTED: %d\nACTUAL: %d\n", ans_ICR, ICR);
            return;
        } else if (flag != flag_ans) {
            fprintf(stdout, "INCORRECT flag\nEXPECTED: %d\nACTUAL: %d\n", flag_ans, flag);
            return;
        }

        flag = 0;
    }

    fprintf(stdout, "SUCCESS!\n");
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

    test_main(realStdout);

    if (errno) {
        fprintf(realStdout, "Error: %d\n", errno);
    }
    return errno;
}
