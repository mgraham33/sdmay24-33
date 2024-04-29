import itertools

#function to convert decimal to binary
def decimalToBinary(n):
    return bin(n)

#function to convert binary to decimal
def binaryToDecimal(n):
    return int(n,2)

#function to convert decimal to hex
def decimalToHex(n):
    return hex(n)

#function to convert hex to decimal
def hexToDecimal(n):
    return int(n,16)

#function to convert hex to binary
def hexToBinary(n):
    return bin(int(n, 16))

#function to convert binary to hex
def binaryToHex(n):
    return hex(int(n, 2))

#signed value to hex function
def signedToHex(n):
    if n < 0:
        return hex((1 << 16) + n)
    else:
        return hex(n)

#hex to signed decimal function
def hexToSignedDecimal(hexval):
    if hexval & (1 << (16 - 1)):
        hexval = hexval - (1 << 16)
    return hexval

#signed decimal to binary function
def signedToBinary(n):
    if n < 0:
        return bin((1 << 16) + n)
    else:
        return bin(n)

def convert(expression):
    binary = False
    hexval = False
    decimal = False
    letter = False

    compound = False

    val = 0

    ret  = []

    expression = expression.split()
    
    #remove ; from last element
    expression[-1] = expression[-1].replace(";", "")

    #if one of the element is only + - * / then it is a compound expression
    for i in expression:
        if i == '+' or i == '-' or i == '*' or i == '/':
            compound = True

    #check if last element is decimal, hex, or binary
    if expression[-1].isdigit() or expression[-1].startswith('-'):
        decimal = True
    elif expression[-1].startswith("0x"):
        hexval = True
    elif expression[-1].startswith("0b"):
        binary = True
    elif expression[-1].startswith("'"):
        letter = True

    if letter:
        decimal = True
        expression[-1] = ord(expression[-1].replace("'", ""))

    if compound == False:
        if "signed" in expression:
            #if decimal convert to hex and binary
            if decimal:
                ret.append(int(expression[-1]))
                ret.append(signedToHex(int(expression[-1])))
                ret.append(signedToBinary(int(expression[-1])))
            elif hexval:
                ret.append(hexToSignedDecimal(int(expression[-1], 16)))
                ret.append(expression[-1])
                ret.append(hexToBinary(expression[-1]))
            elif binary:
                ret.append(binaryToDecimal(expression[-1]))
                ret.append(binaryToHex(expression[-1]))
                ret.append(expression[-1])
        else:
            #if decimal convert to hex and binary
            if decimal:
                ret.append(int(expression[-1]))
                ret.append(decimalToHex(int(expression[-1])))
                ret.append(decimalToBinary(int(expression[-1])))
            elif hexval:
                ret.append(hexToDecimal(expression[-1]))
                ret.append(expression[-1])
                ret.append(hexToBinary(expression[-1]))
            elif binary:
                ret.append(binaryToDecimal(expression[-1]))
                ret.append(binaryToHex(expression[-1]))
                ret.append(expression[-1])
    elif compound == True:
        if expression[-1 - 2].startswith("0x") and expression[-1].startswith("0x"):
            val = (hexToDecimal(expression[-1 - 2]) + hexToDecimal(expression[-1]))
        elif expression[-1 - 2].startswith("0x") and expression[-1].isdigit():
            sign = expression[-1 - 1]
            if sign == '+':
                val = (hexToDecimal(expression[-1 - 2]) + int(expression[-1]))
            elif sign == '-':
                val = (hexToDecimal(expression[-1 - 2]) - int(expression[-1]))
            elif sign == '*':
                val = (hexToDecimal(expression[-1 - 2]) * int(expression[-1]))
            elif sign == '/':
                val = (hexToDecimal(expression[-1 - 2]) / int(expression[-1]))

        #replace last 3 elements with result
        expression[-1 - 2] = val
        expression[-1 - 1] = ""
        expression[-1] = ""
        #remove empty elements
        expression = list(filter(None, expression))
        
        ret.append((expression[-1]))
        ret.append(decimalToHex(int(expression[-1])))
        ret.append(decimalToBinary(int(expression[-1])))

    return ret

def main():
    a = "unsigned short x = 0x2050 + 0x2041;"
    b = "unsigned char x = 20;"

    print(signedToBinary(-8))
    print(signedToHex(-8))

    print(convert(a))
    print(convert(b))


    list1 = ["unsigned", "signed"]
    #list2 = ["char", "short"]
    # # #list with range -128 to 255
    # # list3 = [i for i in range(-128, 256)]
    # # #list with range 'A' to 'Z'
    # # list4 = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    # # #list with range 'a' to 'z'
    # # list5 = [chr(i) for i in range(ord('a'), ord('z')+1)]
    # # #list with range 0x0000 to 0xFFFF
    list6 = [hex(i) for i in range(0x000a, 0xAFFF+1)]
    # # #list with range 00000000 to 11111111 with no padding
    #list7 = [bin(i) for i in range(0, 255+1)]
    # #list with range 00000000 to 11111111 with padding
    # list8 = [format(i, '08b') for i in range(0, 255+1)]
    list9 = [i for i in range(2, 10)]
    # # #list for '+' '-' '*' '/' operations
    list10 = ['+', '-', '*', '/']
    # # #list with range 0x000A to 0x01F4 10 to 500
    # #list11 = [hex(i) for i in range(0x000A, 0x01F4+1)]


    # list6 = [hex(i) for i in range(0x000A, 0xFFFF+1)]

    # # outputslistNums = list(itertools.product(list1, list2, list3))
    # # outputslistChars = list(itertools.product(list1, list2, list4))
    # # outputslistChars2 = list(itertools.product(list1, list2, list5))
    # # outputslistHex = list(itertools.product(list1, list2, list6))
    #outputslistbinnopadding = list(itertools.product(list1, list2, list7))
    # outputslistbinpadding = list(itertools.product(list1, list2, list8))
    outputslisthexops = list(itertools.product(list1, ['short'], list6, list10, list9))

    # #out = list(itertools.combinations(list11, 2))
    

    # #outputslisthexaddition = list(itertools.product(['unsigned'], ['short'], list11, ['+'], list11))

    # # with open("output.txt", "w") as f:
    # #     for item in outputslistNums:
    # #         f.write("%s %s x = %s;\n" % item)
    
    # # with open("outputchars.txt", "w") as f:
    # #     for item in outputslistChars:
    # #         f.write("%s %s x = '%s';\n" % item)
    
    # # with open("outputchars2.txt", "w") as f:
    # #     for item in outputslistChars2:
    # #         f.write("%s %s x = '%s';\n" % item)

    # # with open("outputhex.txt", "w") as f:
    # #     for item in outputslistHex:
    # #         f.write("%s %s x = %s;\n" % item)

    # with open("outputbinnopadding.txt", "w") as f:
    #     for item in outputslistbinnopadding:
    #         f.write("%s %s x = %s;\n" % item)

    # with open("outputbinpadding.txt", "w") as f:
    #     for item in outputslistbinpadding:
    #         f.write("%s %s x = 0b%s;\n" % item)

    with open("outputhexops.txt", "w") as f:
        for item in outputslisthexops:
            #if item[2] % item[4] == 0:
            hexs = int(item[2], 16)
            div = int(item[4])
            if hexs % div == 0 and item[3] == '/':
                f.write("%s %s x = %s %s %s;\n" % item)
            elif item[3] != '/':
                f.write("%s %s x = %s %s %s;\n" % item)

    # with open("outputhexaddition.txt", "w") as f:
    #     for item in outputslisthexaddition:
    #         f.write("%s %s x = %s %s %s;\n" % item)


if __name__ == "__main__":
    main()
