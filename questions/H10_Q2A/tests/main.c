#include "main.h"

extern void init_TIMER1();

unsigned int period = 0;
unsigned int duty = 0;

int test_init_timer(FILE *out) {
    resetCounters(0);
    answer_init_TIMER1(period, duty);
    fill_answers();
    reuse_originals();

    resetCounters(0);

    init_TIMER1();
    fill_tests();
    reuse_originals();

    int failFlag = 1;
    if (!getTimerDisable()) {
        fprintf(out, "Error: didn't properly disable TIMER1_CTL_R during configuration.\nDid you forget to call 'wait_timer_disable()'?\n");
        failFlag = 0;
    }
    return check_answers(out) && failFlag;
}

void failed(FILE *out, const char *message, int *flag, ...) {
    fprintf(out, "%s", message);
    *flag = 1;
}

int main(int argc, char *argv[]) {
    srand(time(NULL));
    scanf("%d\n", &period);
    scanf("%d\n", &duty);

    /* Saves stdout in a new file descriptor */
    int realStdoutNo = dup(STDOUT_FILENO);
    FILE *realStdout = fdopen(realStdoutNo, "w");

    /* Switches stdout/stderr to point to different file descriptor to
    * avoid students passing code by printing the correct result. */
    int devNull = open("/dev/null", O_WRONLY);
    dup2(devNull, STDOUT_FILENO);
    dup2(devNull, STDERR_FILENO);

    int failFlag = 0;
    int i;
    for (i = 0; i < 100; i++) {
        randomize_registers();

        if (!test_init_timer(realStdout)) failed(realStdout, "Timer initialization failed.\n\n", &failFlag);

        if (failFlag) return 0;
    }

    fprintf(realStdout, "Success!\n");
    return 0;
}
