#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>

#include "answer.c"

extern unsigned char q1(unsigned char CAMERA_CONFIG);
extern int q2(unsigned char CAMERA_DATA);
extern unsigned char q3(unsigned char CAMERA_CONFIG);

void testQ1(FILE *stdout) {
    unsigned char CAMERA_CONFIG;
    unsigned char expected;
    unsigned char actual;
    int i = 0;
    for (i = 0; i < 100; i++) {
        CAMERA_CONFIG = ((unsigned char) rand()) & 0x30;
        expected = answer1(CAMERA_CONFIG);
        actual = q1(CAMERA_CONFIG);
        if (expected != actual) {
            fprintf(stdout, "QUESTION 1 FAILED: {CAMERA_CONFIG: %d, EXPECTED: %d, ACTUAL: %d}\n", CAMERA_CONFIG, expected, actual);
            return;
        }
    }
    fprintf(stdout, "QUESTION 1 PASSED\n");
}

void testQ2(FILE *stdout) {
    unsigned char CAMERA_DATA;
    unsigned char expected;
    unsigned char actual;
    int i = 0;
    for (i = 0; i < 100; i++) {
        CAMERA_DATA = (unsigned char) rand();
        expected = answer2(CAMERA_DATA);
        actual = q2(CAMERA_DATA);
        if (expected != actual) {
            fprintf(stdout, "QUESTION 2 FAILED: {CAMERA_DATA: %d, EXPECTED: %d, ACTUAL: %d}\n", CAMERA_DATA, expected, actual);
            return;
        }
    }
    fprintf(stdout, "QUESTION 2 PASSED\n");
}

void testQ3(FILE *stdout, unsigned char maskOnes, unsigned char maskZeroes) {
    unsigned char CAMERA_CONFIG;
    unsigned char expected;
    unsigned char actual;
    int i = 0;
    for (i = 0; i < 100; i++) {
        CAMERA_CONFIG = (unsigned char) rand();
        expected = answer3(CAMERA_CONFIG, maskOnes, maskZeroes);
        actual = q3(CAMERA_CONFIG);
        if (expected != actual) {
            fprintf(stdout, "QUESTION 3 FAILED: {CAMERA_CONFIG: %d, EXPECTED: %d, ACTUAL: %d}\n", CAMERA_CONFIG, expected, actual);
            return;
        }
    }
    fprintf(stdout, "QUESTION 3 PASSED\n");
}

int main(int argc, char *argv[]) {
  
  int n;

  /* Saves stdout in a new file descriptor */
  int realStdoutNo = dup(STDOUT_FILENO);
  FILE *realStdout = fdopen(realStdoutNo, "w");

  /* Switches stdout/stderr to point to different file descriptor to
   * avoid students passing code by printing the correct result. */
  int devNull = open("/dev/null", O_WRONLY);
  dup2(devNull, STDOUT_FILENO);
  dup2(devNull, STDERR_FILENO);
  
  FILE *inputsfile = fopen("inputs.txt", "r");
  if (!inputsfile) {
    fprintf(realStdout, "Error: file not found 'inputs.txt'\n");
    return 1;
  }

  scanf("%d", &n);
  switch(n) {
    case 1: { // Test question 1
        fprintf(realStdout, "Case 1\n");
        testQ1(realStdout);
        break;
    }
    case 2: { // Test question 2
        testQ2(realStdout);
        break;
    }
    case 3: { // Test question 3
        fscanf(inputsfile, "%d", &n); // q3 any1 mask
        unsigned short maskOnes = (unsigned short) n;
        fscanf(inputsfile, "%d", &n); // q3 any0 mask
        unsigned short maskZeroes = (unsigned short) n;
        testQ3(realStdout, maskOnes, maskZeroes);
        break;
    }
  }

  fclose(inputsfile);
  return 0;
}
