#ifndef UTIL_H_
#define UTIL_H_
#include <stdio.h>
#include <stdlib.h>
#include "globals.h"

void set_handler(void (*handler)());
int continue_grading();
void print_pixel_count(int pixelCount);

int getMulticalls();
int getCleared();
int checkCount(FILE *out);

#endif
