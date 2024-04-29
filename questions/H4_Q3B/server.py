import random, math

def generate(data):
    resolutions = {
        '100x100': 0,
        '320x240': 1,
        '640x480': 2,
        '1280x1024':3
    }

    speeds = {
        '1': 0,
        '30': 1,
        '60': 2,
        '120': 3,
        '240': 4
    }

    resolution = random.choice(list(resolutions.keys()))
    speed = random.choice(list(speeds.keys()))

    data['params']['resolution'] = resolution
    data['params']['speed'] = speed
    temp = resolutions[resolution] << 4 | speeds[speed] << 1
    data['params']['maskOnes'] = temp
    data['params']['maskZeroes'] = temp | 0xc1
    data['params']['maskones_c'] = "0x%0.4X" % temp
    data['params']['maskzeroes_c'] = "0x%0.4X" % (temp | 0xc1)


     
def generateMASK(bitList):
    temp = 0
    for bit in bitList:
        temp = temp | (1 << bit)
    return temp

def generateINVERSEMASK(bitList, length):
    if (length == 'char'): return (~generateMASK(bitList)) & 0xFF
    if (length == 'short'): return (~generateMASK(bitList)) & 0xFFFF

