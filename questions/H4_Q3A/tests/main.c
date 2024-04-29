#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>

#include "answer.c"

extern int q1(unsigned char ch);
extern unsigned short q2(unsigned short n);
extern int q3(unsigned short n);
extern unsigned char q4(unsigned char ch); 

void testQ1(FILE *stdout, unsigned char check) {
    unsigned char ch;
    int expected;
    int actual;
    int i = 0;
    for (i = 0; i < 100; i++) {
        ch = (unsigned char) rand();
        expected = answer1(ch, check);
        actual = q1(ch);
        if (expected != actual) {
            fprintf(stdout, "QUESTION 1 FAILED: {CH: %d, EXPECTED: %d, ACTUAL: %d}\n", ch, expected, actual);
            return;
        }
    }
    fprintf(stdout, "QUESTION 1 PASSED\n");
}

void testQ2(FILE *stdout, unsigned short set, unsigned short clear, unsigned short toggle) {
    unsigned short n;
    int expected;
    int actual;
    int i = 0;
    for (i = 0; i < 100; i++) {
        n = (unsigned short) rand();
        expected = answer2(n, set, clear, toggle);
        actual = q2(n);
        if (expected != actual) {
            fprintf(stdout, "QUESTION 2 FAILED: {N: %d, EXPECTED: %d, ACTUAL: %d}\n", n, expected, actual);
            return;
        }
    }
    fprintf(stdout, "QUESTION 2 PASSED\n");
}

void testQ3(FILE *stdout, unsigned short all1, unsigned short all0, unsigned short any1, unsigned short any0) {
    unsigned short n;
    int expected;
    int actual;
    int i = 0;
    for (i = 0; i < 100; i++) {
        n = (unsigned short) rand();
        expected = answer3(n, all1, all0, any1, any0);
        actual = q3(n);
        if (expected != actual) {
            fprintf(stdout, "QUESTION 3 FAILED: {N: %d, EXPECTED: %d, ACTUAL: %d}\n", n, expected, actual);
            return;
        }
    }
    fprintf(stdout, "QUESTION 3 PASSED\n");
}

void testQ4(FILE *stdout, int rotate) {
    unsigned char ch;
    int expected;
    int actual;
    int i = 0;
    for (i = 0; i < 100; i++) {
        ch = (unsigned char) rand();
        expected = answer4(ch, rotate);
        actual = q4(ch);
        if (expected != actual) {
            fprintf(stdout, "QUESTION 4 FAILED: {CH: %d, EXPECTED: %d, ACTUAL: %d}\n", ch, expected, actual);
            return;
        }
    }
    fprintf(stdout, "QUESTION 4 PASSED\n");
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
        fscanf(inputsfile, "%d", &n); // q1 mask
        unsigned char check = (unsigned char) n;
        testQ1(realStdout, check);
        break;
    }
    case 2: { // Test question 2
        fscanf(inputsfile, "%d", &n); // q2 set mask
        unsigned short set = (unsigned short) n;
        fscanf(inputsfile, "%d", &n); // q2 clear mask
        unsigned short clear = (unsigned short) n;
        fscanf(inputsfile, "%d", &n); // q2 toggle mask
        unsigned short toggle = (unsigned short) n;
        testQ2(realStdout, set, clear, toggle);
        break;
    }
    case 3: { // Test question 3
        fscanf(inputsfile, "%d", &n); // q3 all1 mask
        unsigned short all1 = (unsigned short) n;
        fscanf(inputsfile, "%d", &n); // q3 all0 mask
        unsigned short all0 = (unsigned short) n;
        fscanf(inputsfile, "%d", &n); // q3 any1 mask
        unsigned short any1 = (unsigned short) n;
        fscanf(inputsfile, "%d", &n); // q3 any0 mask
        unsigned short any0 = (unsigned short) n;
        testQ3(realStdout, all1, all0, any1, any0);
        break;
    }
    case 4: { // Test question 4
        fscanf(inputsfile, "%d", &n); // q4 rotate value
        testQ4(realStdout, n);
        break;
    }
  }

  fclose(inputsfile);
  return 0;
}
