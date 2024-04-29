#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

FILE *realStdout;
#define UNSIGNED_CHAR_SIZE 16
unsigned char max_consecutive_1s(unsigned short x);

unsigned char ans(unsigned short x){
    int index = 0;
    unsigned char longestCount = 0;
    int currentCount = 0;
    
    while(index <= UNSIGNED_CHAR_SIZE){
        if(x & (1<<index))
            currentCount++;
        else{
            if(currentCount > longestCount)
                longestCount = currentCount;
            currentCount = 0;
        }
        index++;
    }
   return longestCount;
}

int main(void){
	
	int realStdoutNo = dup(STDOUT_FILENO);
    realStdout = fdopen(realStdoutNo, "w");

    int devNull = open("/dev/null", O_WRONLY);
    dup2(devNull, STDOUT_FILENO);
    dup2(devNull, STDERR_FILENO);

    unsigned short testingList[] = {
        0xFF5F, 0x77FE, 0x2310, 0xFFFF, 0x0101
    };
    
    for(int i = 0; i < 5; i++){
         fprintf(realStdout, "TEST %d ", i+1);
        if(ans(testingList[i]) == max_consecutive_1s(testingList[i]))
            fprintf(realStdout, "PASSED\n");
        else
            fprintf(realStdout, "FAILED\n");
    }

    return 0;
}