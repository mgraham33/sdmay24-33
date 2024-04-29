#include <stdio.h>
#include <stdlib.h>


int char_count(char* str1, char char1){
    int i = 0;
    int count = 0;

    while(str1[i] != 0){
        if(str1[i] == char1){
            count++;
        }
        i++;
    }
    return count;
}