// Example of using function char_count() to find how many times
// character ‘d’ occurs in string “hello world”.
#include <stdio.h>
int main(void)
{
  char my_str_tmp[] = "hello world";
  char my_char_tmp = 'd';
  int my_count = 0;
  my_count = char_count(my_str_tmp, my_char_tmp);
  printf("%s. has %c %d times \n", my_str_tmp, my_char_tmp, my_count);
}