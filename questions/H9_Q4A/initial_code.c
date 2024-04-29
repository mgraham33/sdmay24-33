#include <stdio.h>
#include <stdlib.h>

Config_Timer1()
{
    // 1. Setup GPIO
    // A. Configure GPIO module associated with Timer 1 A
    // Since A or B was not specified either is fine. I used A
    // i. Turn on clock for GPIO Port B
    // Note: Timer 1A can use Port B or F, this solution uses Port B
    // Note: Port F would use different pins of its port.
    SYSCTL_RCGCGPIO_R = SYSCTL_RCGCGPIO_R | 0b000010; // 0x02
    // ii.Enable Alternate function and set Peripheral functionality
    GPIO_PORTB_AFSEL_R |= 0b0001_0000; // Timer1 A Input is on bit 4
    GPIO_PORTB_PCTL_R |= 0x0007_0000;  // use Timer input for wire 4
    // iii. set digital or analog mode, and pin directions
    GPIO_PORTB_DEN_R |= 0b0001_0000; // enable pin 4 digital mode
    GPIO_PORTB_DIR_R &= 0b1110_1111; // set pin 4 to input
    // 2. Setup Timer 1 A
    // A) Configure Timer 1 mode
    SYSCTL_RCGCTIMER_R |= 0b0000_0010; // Enable Timer 1’s clock
    // Disable Timer 1 device while we set it up
    TIMER1_CTL_R &= 0xFFFE;
    // Set desired Timer 1 functionality
    TIMER1_CFG_R = 0x4;          // Set to 16-bit mode
    TIMER1_TAMR_R = 0b0001_0111; // Count up,Edge-Time Mode,Capture Mode
    TIMER1_CTL_R = 0b0000_0000;  // Detect positive edges
    TIMER1_TAPR_R = FF;          // set timer prescaler(extended timer) and load
    TIMER1_TAILR_R = 0xFFFF      // init value to max 24-bit Timeout value
        // B) Setup Timer 1 Interrupts
        TIMER1_ICR_R |= 0b0000_0100; // Clear Event Capture interupt status
    TIMER1_IM_R |= 0b0000_0100;      // Enable Event Capture interrupts
    // 3. NVIC setup
    // A) Configure NVIC to allow Timer 1A interrupts
    // Note: Priority was not specified so any priority is fine.
    NVIC_PRI5_R |= 0x0000_2000; // Timer1A IRQ Pri to 1 Grp5 bits 15-13
    NVIC_EN0_R |= 0x0020_0000;  // Enable Timer 1A IRQ(ie.IRQ21):set bit 21
    // B) Bind Timer 1A interrupt requests to User’s Interrupt Handler
    IntRegister(INT_TIMER1A, Timer_1_Handler);
    // re-enable Timer 1A
    TIMER1_CTL_R |= 0x0001;
}
