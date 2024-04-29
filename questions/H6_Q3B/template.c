#include "/grade/tests/student.h" // Required to compile. Links your code with the grader

// You may declare additional variables here.

/**
 * ISR that services the Camera Controller's interrupts
 */
void CAMERA_HANDLER()
{
    // TODO
}

void student_main() 
{
    Camera_Configure();         // Configures the camera

    // Limits the number of loop iterations
    while (continue_grading())
    {
        // TODO
    }
}
