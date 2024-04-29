#include "main.h"

void test(FILE *stdout) {
    student_main();

    int failed = 0;
    if (!getCleared()) {
        fprintf(stdout, "Error, incorrect CAMERA_INT_EN_CLR register.\n\n");
        failed = 1;
    }
    if (getMulticalls()) {
        fprintf(stdout, "Error, you called 'print_pixel_count()' multiple times per loop.\n\n");
        failed = 1;
    }
    checkCount(stdout);

    if (failed) {
        fprintf(stdout, "ERROR!\n");
    } else {
        fprintf(stdout, "SUCCESS!\n");
    }
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

    set_handler(CAMERA_HANDLER);
    CAMERA_INT_EN_CLR = rand() & ~0x10;

    test(realStdout);

    if (errno) {
        fprintf(realStdout, "Error: %d\n", errno);
    }
    return errno;
}
