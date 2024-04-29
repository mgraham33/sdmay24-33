import random, math

def generate(data):
    bits_char = [0, 1, 2, 3, 4, 5, 6, 7]
    bits_short = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    inputs = []

    random.shuffle(bits_char)
    q1a = bits_char[:random.randint(2, 4)]
    q1a.sort()
    data['params']['q1a'] = str(q1a)
    mask = generateMASK(q1a)
    inputs.append(mask)
    data['params']['ans_q1a'] = "0x%0.2X" % mask


    random.shuffle(bits_short)
    t0 = random.randint(2, 4)
    t1 = random.randint(t0 + 2, t0 + 4)
    t2 = random.randint(t1 + 2, t1 + 4)
    q1bset = bits_short[:t0]
    q1bclear = bits_short[t0:t1]
    q1btoggle = bits_short[t1:t2]
    q1bset.sort()
    q1bclear.sort()
    q1btoggle.sort()
    data['params']['q1bset'] = str(q1bset)
    data['params']['q1bclear'] = str(q1bclear)
    data['params']['q1btoggle'] = str(q1btoggle)
    mask = generateMASK(q1bset)
    inputs.append(mask)
    data['params']['ans_set_q1b'] = "0x%0.4X" % mask
    mask = generateMASK(q1bclear)
    inputs.append(mask)
    data['params']['ans_clear_q1b'] = "0x%0.4X" % mask
    mask = generateMASK(q1btoggle)
    inputs.append(mask)
    data['params']['ans_toggle_q1b'] = "0x%0.4X" % mask

    random.shuffle(bits_short)
    t0 = random.randint(2, 4)
    t1 = random.randint(t0 + 2, t0 + 4)
    t2 = random.randint(t1 + 2, t1 + 4)
    t3 = random.randint(t2 + 2, t2 + 3)
    q1callset = bits_short[:t0]
    q1callclear = bits_short[t0:t1]
    q1canyset = bits_short[t1:t2]
    q1canyclear = bits_short[t2:t3]
    q1callset.sort()
    q1callclear.sort()
    q1canyset.sort()
    q1canyclear.sort()
    data['params']['q1callset'] = str(q1callset)
    data['params']['q1callclear'] = str(q1callclear)
    data['params']['q1canyset'] = str(q1canyset)
    data['params']['q1canyclear'] = str(q1canyclear)
    mask = generateMASK(q1callset)
    inputs.append(mask)
    data['params']['ans_all1_q1c'] = "0x%0.4X" % mask
    mask = generateMASK(q1callclear)
    inputs.append(mask)
    data['params']['ans_all0_q1c'] = "0x%0.4X" % mask
    mask = generateMASK(q1canyset)
    inputs.append(mask)
    data['params']['ans_any1_q1c'] = "0x%0.4X" % mask
    mask = generateMASK(q1canyclear)
    inputs.append(mask)
    data['params']['ans_any0_q1c'] = "0x%0.4X" % mask
    
    rotate = random.randint(1, 4)
    data['params']['q1d'] = f"{rotate} position{'s' if rotate != 1 else ''} (bit 0 should end up at bit position {8 - rotate})"
    inputs.append(rotate)
    data['params']['ans_right_q1d'] = "0x%0.2X" % rotate
    rotate = 8 - rotate
    data['params']['ans_left_q1d'] = "0x%0.2X" % rotate

    data['params']['inputs_part1'] = inputs

     
def generateMASK(bitList):
    temp = 0
    for bit in bitList:
        temp = temp | (1 << bit)
    return temp

def generateINVERSEMASK(bitList, length):
    if (length == 'char'): return (~generateMASK(bitList)) & 0xFF
    if (length == 'short'): return (~generateMASK(bitList)) & 0xFFFF

