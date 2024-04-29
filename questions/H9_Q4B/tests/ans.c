#include <stdio.h>
#include <stdlib.h>

// Count the number of occurrences of char1 in a null terminated c-string str1
// if size is less than or equal to 1 return -1
// if char is not found return -2
int char_count(char *str1, char char1)
{
    // find size
    int i = 0;
    int count = 0;
    char *temp = str1;

    while (*temp)
    {

        temp++;
        i++;
    }

    // first case
    if (i <= 1)
    {

        return -1;
    }

    // second case
    while (*str1)
    {

        if (*str1 == char1)
        {

            count++;
        }
        str1++;
    }

    if (count == 0)
    {
        return -2;
    }

    return count;
}
