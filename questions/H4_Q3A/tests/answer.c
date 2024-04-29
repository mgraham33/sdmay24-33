int answer1(unsigned char ch, char check) {
    if (ch & check) return 1;
    return 0;
}

unsigned short answer2(
    unsigned short n, 
    unsigned short set, 
    unsigned short clear, 
    unsigned short toggle ) 
{
    return ((n | set) & clear ) ^ toggle;
}

int answer3(
    unsigned short n, 
    unsigned short all1, 
    unsigned short all0,
    unsigned short any1,
    unsigned short any0 ) 
{
    if (
        (n & all1) == all1 &&
        (~n & all0) == all0 &&
        (n & any1) && (~n & any0)
    ) return 1;
    return 0;
}

unsigned char answer4(unsigned char ch, int rotate) {
    return (ch >> rotate) | (ch << (8 - rotate));
}
