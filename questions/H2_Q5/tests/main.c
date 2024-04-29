#include <stdio.h>
#include <stdlib.h>

int char_count(char* str1, char char1);

int main(void)
{

    // test 1
    int test1 = char_count("hello world", 'd');
    if (test1 == 1)
    {
        printf("TEST 1 PASSED\n");
    }

    // test 2
    int test2 = char_count("hello world", 'l');
    if (test2 == 3)
    {
        printf("TEST 2 PASSED\n");
    }

    // test 3
    int test3 = char_count("hello world", 'x');
    if (test3 == 0)
    {
        printf("TEST 3 PASSED\n");
    }

    return 0;
}