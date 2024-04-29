#include "test.h"

#define TRUE 1
#define FALSE 0

/**
 * With the given CAMERA_CONFIG register:
 * Assume the camera is currently set for 1280x1024 resolution.
 * Return the register after updating it to a 100x100 resolution.
 * Preserve the other bits in the register.
 */
unsigned char q1(unsigned char CAMERA_CONFIG) {
    return (TODO1);
}

/**
 * With the given CAMERA_DATA register:
 * Assume it just received a new color pixel. 
 * Check if any of the color components (Red, Green, Blue)
 * have their LEAST significant bit set to 1.
 */
int q2(unsigned char CAMERA_DATA) {
    if (TODO2) {
        return TRUE;
    }
    return FALSE;
}

/**
 * With the given CAMERA_CONFIG register:
 * Set the speed to {{params.speed}} FPS
 * Set the resolution to {{params.resolution}}
 * Enable the camera
 * Preserve all other bits.
 */
unsigned char q3(unsigned char CAMERA_CONFIG) {
    return (TODO3);
}
