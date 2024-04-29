#include "util.h"

int bMulticalls = 0;
int bToClear = 0;
int bCleared = 1;
int pixelCount = 0;
int studentPixelCount = 0;
int loopiters = 100;

void (*pHandler)();

void set_handler(void (*handler)()) {
    pHandler = handler;
}

int continue_grading() {
    if (!loopiters--) return 0;

    if (bToClear ^ ((CAMERA_INT_EN_CLR >> 4) & 0x1)) {
        bCleared = 0;
    }
    
    CAMERA_INT_EN_CLR &= ~0x10;
    if (rand() & 1) {
        CAMERA_CMD_STAT = 0x40;
        pixelCount++;
        bToClear = 1;
    } else {
        CAMERA_CMD_STAT = 0;
        bToClear = 0;
    }
    pHandler();
    return 1;
}

void print_pixel_count(int pixelCount) {
    if (studentPixelCount == pixelCount) bMulticalls = 1;
    studentPixelCount = pixelCount;
}

int getMulticalls() {
    return bMulticalls;
}

int getCleared() {
    return bCleared;
}

int checkCount(FILE *out) {
    if (pixelCount != studentPixelCount) {
        fprintf(out, "Error, incorrect pixel count.\nExpected %d, got %d.\n\n", pixelCount, studentPixelCount);
        return 0;
    }
    return 1;
}
