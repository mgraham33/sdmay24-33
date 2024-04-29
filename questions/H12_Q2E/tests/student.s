.global _arrays
_arrays:                                // Start of the function
    movw r0, #0x0dcc
    movt r0, #0x2000
    
    movw r1, #0x0964
    movt r1, #0x2000
    
    ldr r2, [r1]
    ldrb r3, [r2]
    
    add r3, #3
    
    strb r3, [r0, #0]
    
    bx lr                               // Returns from the function