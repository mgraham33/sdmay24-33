
#include "main.h"

extern void get_sensor_reading(int *left_sensor, int *right_sensor);
extern void set_motor_speed(int left_motor, int right_motor);
extern void compute_motor_values(int left_sensor, int right_sensor, int *left_motor, int *right_motor);

int test_sensor_reading(FILE *out) {
    int left_sensor;
    int right_sensor;
    int ans_left_sensor;
    int ans_right_sensor;
    resetCounters(0);
    answer_get_sensor_reading(&ans_left_sensor, &ans_right_sensor);
    fill_answers();
    reuse_originals();

    int count = 0;
    if (~ADC0_RIS_R & 0x1) count = (rand() % 5) + 1;
    resetCounters(count);

    get_sensor_reading(&left_sensor, &right_sensor);
    fill_tests();
    reuse_originals();

    int failFlag = 1;
    if (left_sensor != ans_left_sensor || right_sensor != ans_right_sensor) {
        fprintf(out, "Error: incorrect left or right sensor values; Expected '0x%08X:0x%08X', got '0x%08X:0x%08X'\n", ans_left_sensor, ans_right_sensor, left_sensor, right_sensor);
        failFlag = 0;
    }
    if (getADCWaitCount() != 0) {
        fprintf(out, "Error: incorrect busy-wait.\nDid you forget to call 'wait_adc()'?\n");
        failFlag = 0;
    }
    return check_answers(out) && failFlag;
}

int test_motor_speed(FILE *out) {
    int left_motor = (rand() % 99) + 1;
    int right_motor = (rand() % 99) + 1;

    answer_set_motor_speed(left_motor, right_motor);
    fill_answers();
    reuse_originals();

    set_motor_speed(left_motor, right_motor);
    fill_tests();
    reuse_originals();

    return check_answers(out);
}

int test_compute_motors(FILE *out) {
    int left_sensor = (rand() % 0xfff) + 1;
    int right_sensor = (rand() % 0xfff) + 1;
    int left_motor;
    int right_motor;
    int ans_left_motor;
    int ans_right_motor;

    answer_compute_motor_values(left_sensor, right_sensor, &ans_left_motor, &ans_right_motor);
    compute_motor_values(left_sensor, right_sensor, &left_motor, &right_motor);

    if (left_motor != ans_left_motor || right_motor != ans_right_motor) {
        fprintf(out, "Error: incorrect motor values given sensors '0x%08X:0x%08X'; Expected '0x%08X:0x%08X', got '0x%08X:0x%08X'\n", left_sensor, right_sensor, ans_left_motor, ans_right_motor, left_motor, right_motor);
        return 0;
    }
    return 1;
}

void test(int boolean, FILE *out, const char *fail_message, int *fail_flag) {
    if (boolean) {
        // fprintf(out, "%s", success_message);
    } else {
        fprintf(out, "%s", fail_message);
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

        test(test_sensor_reading(realStdout), realStdout, "Sensor reading failed.\n\n", &failFlag);
        test(test_compute_motors(realStdout), realStdout, "Motor speed computation failed.\n\n", &failFlag);
        test(test_motor_speed(realStdout), realStdout, "Motor speed set failed.\n\n", &failFlag);

        if (failFlag) return 0;
    }

    fprintf(realStdout, "Sensor reading succeeded.\n\n");
    fprintf(realStdout, "Motor speed computation succeeded.\n\n");
    fprintf(realStdout, "Motor speed set succeeded.\n\n");
    return 0;
}
