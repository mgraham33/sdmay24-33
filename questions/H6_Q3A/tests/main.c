#include "main.h"

void test_config(FILE *stdout, unsigned int configMask, unsigned int intMask) {
    CAMERA_CMD_STAT = 1;
    Camera_Configure();
    if (CAMERA_CONFIG != configMask) {
        fprintf(stdout, "INCORRECT CAMERA_CONFIG\nEXPECTED: 0x%X\nACTUAL: 0x%X\n", configMask, CAMERA_CONFIG);
        return;
    } else if (CAMERA_INT_EN_CLR != intMask) {
        fprintf(stdout, "INCORRECT CAMERA_INT_EN_CLR\nEXPECTED: 0x%X\nACTUAL: 0x%X\n", intMask, CAMERA_INT_EN_CLR);
        return;
    } else if (waited() != 1 || CAMERA_CMD_STAT != 0) {
        fprintf(stdout, "FAILED TO WAIT FOR CONFIGURATION UPDATE\nDid you forget to call 'wait()' in your busy-loop?\n");
        return;
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

    unsigned int configMask = 0;
    unsigned int intMask = 0;
    scanf("%d", &configMask);
    scanf("%d", &intMask);

    test_config(realStdout, configMask, intMask);

    if (errno) {
        fprintf(realStdout, "Error: %d\n", errno);
    }
    return errno;
}
