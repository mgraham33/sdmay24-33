#include "main.h"

int done_testing = 0;

void test_main(FILE *stdout) {

    if (flag != 0)
    {
        fprintf(stdout, "INCORRECT flag\nEXPECTED: %d\nACTUAL: %d\n", 0, flag);
        return;
    }

    fprintf(stdout, "SUCCESS!\n");
}

void init_portB() {

}

void serial_init() {

}

void lprintf() {
    
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
