#include "/grade/tests/student_uart.h" // Required to compile. Links your code with the grader

void My_UART0_Handler();
void serial_init(void);

volatile int flag = 0; // Helper variable

int main()
{
    init_portB(); // Assume implemented correctly in Question 2
    serial_init();

    while (1)
    {

        // Print each time the LED is turned ON or OFF
        // Hint: make use the helper variable flag declared above.
        //  YOUR CODE HERE
    }

    return 0;
}
