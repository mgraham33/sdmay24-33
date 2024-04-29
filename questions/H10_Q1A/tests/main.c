
#include "main.h"

extern void init_TIMER1_A_B();

int test_init_timer(FILE *out) {
    answer_init_TIMER1_A_B();
    fill_answers();
    reuse_originals();

    resetCounters(0);

    init_TIMER1_A_B();
    fill_tests();
    reuse_originals();

    int failFlag = 1;
    if (!getTimerDisable()) {
        fprintf(out, "Error: didn't properly disable TIMER1_CTL_R during configuration.\nDid you forget to call 'wait_timer_disable()'?\n");
        failFlag = 0;
    }
    return check_answers(out) && failFlag;
}

void test(int boolean, int *fail_flag) {
    if (!boolean) {
        *fail_flag = 1;
    }
}

int main(int argc, char *argv[]) {
    srand(time(NULL));

    /* Saves stdout in a new file descriptor */
    int realStdoutNo = dup(STDOUT_FILENO);
    FILE *realStdout = fdopen(realStdoutNo, "w");
    // FILE *output = fopen("results", "w");

    /* Switches stdout/stderr to point to different file descriptor to
    * avoid students passing code by printing the correct result. */
    int devNull = open("/dev/null", O_WRONLY);
    dup2(devNull, STDOUT_FILENO);
    dup2(devNull, STDERR_FILENO);

    int failFlag = 0;
    int i;
    for (i = 0; i < 100; i++) {
        randomize_registers();

        test(test_init_timer(realStdout), &failFlag);

        if (failFlag) {
            fprintf(realStdout, "Timer initialization failed.\n");
            return 0;
        }
    }

    fprintf(realStdout, "Timer initialization succeeded.\n");
    return 0;
}
