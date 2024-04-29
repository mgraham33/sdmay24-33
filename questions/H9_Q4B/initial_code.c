#include <stdio.h>
#include <stdlib.h>

// Global variables (you may use additional variables)
volatile unsigned int first_wheel_hit;  // When 1st wheel hits sensor
volatile unsigned int second_wheel_hit; // When 2nd wheel hits sensor
volatile int done_flag = 0;             // 1 after both first and second_wheel_hit
                                        // have been stored
// Store first_wheel_hit and second_wheel_hit
void Timer_1_Handler(void)
{
    static int state = 0; // Using a global instead also fine
    // Check if an edge time capture interrupt occurred
    if (TIMER1_RIS_R & 0b0000_0100)
    {
        // Clear the interrupt
        TIMER1_ICR = 0b0000_0100;
        // Capture rising edge time for when 1st wheel hits sensor
        if (state == 0)
        {
            first_wheel_hit = TIMER1_TAR_R;
            state = 1;
        }
        else // Capture rising edge time for when 2nd wheel hits sensor
        {
            second_wheel_hit = TIMER1_TAR_R;
            done_flag = 1; // tell main done capturing 1st & 2nd wheel times
            state = 0;
        }
    }
}
