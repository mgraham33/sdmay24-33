#include <stdio.h>
#include <stdlib.h>

// Return 1 if the car is not fast enough to jump the gap
int Stop_car(void)
{
    float velocity_car;
    float time;
    // Compute car velocity based on captured times and distance
    // between wheels: d = v*t => v = d/t

    // Assuming at most one overflow, so not dealing with overflow
    // 16 MHz tick rate => .0625us tick period
    time = (second_wheel_hit - first_wheel_hit) * .0625 // In usec
    time = time / 1000000;                          // Time in seconds
    velocity_car = 1.5 / time;                          // In m/s
    // Assume min velocity was computed offline, fine if computed
    // in program. Min_velocity is about 31.2 m/s (see below for
    // one way to compute off-line)
    if (velocity_car < 31.2)
    {
        return 1; // Not fast enough stop
    }
    else
    {
        return 0; // Fast enough make jump
    }
}
