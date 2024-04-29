#ifndef ANSWER_H_
#define ANSWER_H_

#include "globals.h"
#include "util.h"

void answer_init_TIMER1_A_B();
void answer_init_ADC();
void answer_get_sensor_reading(int *left_sensor, int *right_sensor);
void answer_set_motor_speed(int left_motor, int right_motor);
void answer_compute_motor_values(int left_sensor, int right_sensor, int *left_motor, int *right_motor);

#endif