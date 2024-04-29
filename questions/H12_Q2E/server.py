import random, math

def isFilled(map, adr, variable):
    for i in range(variable['width']):
        if adr+i in map:
            return True
    return False

# Generates addresses between 0x2000_0000 and 0x2000_0fff, and keeps track of the mappings
#
# variable is an object with 3 attributes: name, width, and type.
# Type is the type of pointer made in C. i.e. unsigned int, int[5], char, etc.
# Width is the number of 4-byte memory blocks the variable takes up. int = 1, long long = 2, int[5] = 5, etc.
# Name is the name of the variable used in the C code.
def generateAddress(data, variable):
    memoryMap = data['params']['memoryMap']
    base = random.randint(0, 0x3ff)
    while isFilled(memoryMap, base, variable):
        base = (base + 1) % 0x400
    for i in range(variable['width']):
        if i == 0: memoryMap[base] = variable
        else: memoryMap[base+i] = None
    # returns 4-byte-aligned address
    return 0x20000000 | (base<<2)


def generate(data):
    # initializes the addressMap
    data['params']['memoryMap'] = {}

    generateAddress(data, {'name':'ch1','width':1,'type':'unsigned char'})
    # to generate an array, we define a variable and give it the requisite width. It's type is the variable type, NOT a POINTER!
    data['params']['A_adr'] = "0x%0.8X" % generateAddress(data, {'name':'A','width':5,'type':'unsigned char'})
    data['params']['pch_adr'] = "0x%0.8X" % generateAddress(data, {'name':'pch','width':1,'type':'unsigned char *'})
    # generate index for A and increment amount
    data['params']['A_ind'] = random.randint(0, 4)
    data['params']['add_amnt'] = random.randint(1, 9)
