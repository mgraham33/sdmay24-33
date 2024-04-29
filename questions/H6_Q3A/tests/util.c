#include "util.h"

int bWaited = 0;

void wait() {
    CAMERA_CMD_STAT = 0;
    bWaited = 1;
}

int waited() {
    return bWaited;
}
