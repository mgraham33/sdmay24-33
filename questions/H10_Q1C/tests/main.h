#ifndef MAIN_H_
#define MAIN_H_

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include "answer.h"
#include "student.h"
#include "globals.h"
#include "util.h"

void wait_adc();
void wait_adc_disable();
void wait_timer_disable();

#endif
