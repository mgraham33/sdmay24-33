unsigned char answer1(unsigned char CAMERA_CONFIG) {
    return CAMERA_CONFIG & 0xcf;
}

int answer2(unsigned char CAMERA_DATA) {
    return CAMERA_DATA & 0x25 ? 1 : 0;
}

unsigned char answer3(unsigned char CAMERA_CONFIG, unsigned char maskOnes, unsigned char maskZeroes) {
    return (CAMERA_CONFIG | maskOnes) & maskZeroes;
}
