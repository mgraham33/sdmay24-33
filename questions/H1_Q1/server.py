import random, copy, sys
sys.path.append('../../HW1')
from Hw1Q1 import convert

#Written by: Ryan Bumann

def generate(data):

    #The convert function throughout is used to convert a expression whether it is a decimal, hex, or binary to decimal, hex, and binary. And return
    #a list of the decimal, hex, and binary value of the expression. ret[0] is decimal, ret[1] is hex, and ret[2] is binary.


    #open file HW1/output.txt
    nums = open("../../HW1/output.txt", "r")
    #choose random line in file
    #It will choose a signed/unsigned char/short where signed value range is from -128 to 255 and unsigned value range is from 0 to 255
    line = random.choice(nums.readlines())
    data['params']['nums'] = line
    #calc nums to put in answer
    ret = convert(line)
    data['correct_answers']['firstquestiondecimal'] = ret[0]
    data['correct_answers']['firstquestionhex'] = ret[1]
    data['correct_answers']['firstquestionbinary'] = ret[2]
    
    #open file HW1/outputchars.txt
    capletter = open("../../HW1/outputchars.txt", "r")
    #choose random line in file
    #It will choose a random capital letter from A to Z from either signed/unsigned char/short
    line = random.choice(capletter.readlines())
    data['params']['capletter'] = line
    #calc nums to put in answer
    ret = convert(line)
    data['correct_answers']['secondquestiondecimal'] = ret[0]
    data['correct_answers']['secondquestionhex'] = ret[1]
    data['correct_answers']['secondquestionbinary'] = ret[2]

    #open file HW1/output.txt
    nums = open("../../HW1/output.txt", "r")
    #choose random line in file
    #It will choose a signed/unsigned char/short where signed value range is from -128 to 255 and unsigned value range is from 0 to 255
    line = random.choice(nums.readlines())
    data['params']['nums2'] = line
    #calc nums to put in answer
    ret = convert(line)
    data['correct_answers']['thirdquestiondecimal'] = ret[0]
    data['correct_answers']['thirdquestionhex'] = ret[1]
    data['correct_answers']['thirdquestionbinary'] = ret[2]

    #open file HW1/outputhex.txt
    hexnums = open("../../HW1/outputhex.txt", "r")
    #choose random line in file
    #It will choose a random hex number from signed/unsigned char/short from 0x0 to 0xFFFF
    line = random.choice(hexnums.readlines())
    data['params']['hexnums'] = line
    #calc nums to put in answer
    ret = convert(line)
    data['correct_answers']['fourthquestiondecimal'] = ret[0]
    data['correct_answers']['fourthquestionhex'] = ret[1]
    data['correct_answers']['fourthquestionbinary'] = ret[2]

    #open file HW1/outputbinpadding.txt
    binarynum = open("../../HW1/outputbinpadding.txt", "r")
    #choose random line in file
    #It will choose a random padded binary number from signed/unsigned char/short from 0b00000000 to 0b11111111
    line = random.choice(binarynum.readlines())
    data['params']['binarynum'] = line
    ret = convert(line)
    data['correct_answers']['fifthquestiondecimal'] = ret[0]
    data['correct_answers']['fifthquestionhex'] = ret[1]
    data['correct_answers']['fifthquestionbinary'] = ret[2]

    #open file HW1/outputhexaddition.txt
    hexaddition = open("../../HW1/outputhexaddition.txt", "r")
    #choose random line in file
    #It will choose a random hex addition from unsigned short from 0xa + 0xa to 0x1f4 + 0x1f4
    line = random.choice(hexaddition.readlines())
    data['params']['hexaddition'] = line
    #calc nums to put in answer
    ret = convert(line)
    data['correct_answers']['sixthquestiondecimal'] = ret[0]
    data['correct_answers']['sixthquestionhex'] = ret[1]
    data['correct_answers']['sixthquestionbinary'] = ret[2]

    #open file HW1/outputhexops.txt
    hexops = open("../../HW1/outputhexops.txt", "r")
    #choose random line in file
    #It will choose a random hex operation from unsigned/signed short from 0xa - 0xafff, then operated by one of these operations +, -, *, /, then range of 2 - 9
    line = random.choice(hexops.readlines())
    data['params']['hexops'] = line
    #calc nums to put in answer
    ret = convert(line)
    data['correct_answers']['seventhquestiondecimal'] = round(ret[0])
    data['correct_answers']['seventhquestionhex'] = ret[1]
    data['correct_answers']['seventhquestionbinary'] = ret[2]

    #open file HW1/outputhexops.txt
    hexops2 = open("../../HW1/outputhexops.txt", "r")
    #choose random line in file
    #It will choose a random hex operation from unsigned/signed short from 0xa - 0xafff, then operated by one of these operations +, -, *, /, then range of 2 - 9
    line = random.choice(hexops2.readlines())
    data['params']['hexops2'] = line
    ret = convert(line)
    data['correct_answers']['eighthquestiondecimal'] = round(ret[0])
    data['correct_answers']['eighthquestionhex'] = ret[1]
    data['correct_answers']['eighthquestionbinary'] = ret[2]

    #open file HW1/output.txt
    nums = open("../../HW1/output.txt", "r")
    #choose random line in file
    #It will choose a signed/unsigned char/short where signed value range is from -128 to 255 and unsigned value range is from 0 to 255
    line = random.choice(nums.readlines())
    data['params']['nums3'] = line
    #calc nums to put in answer
    ret = convert(line)
    data['correct_answers']['ninthquestiondecimal'] = ret[0]
    data['correct_answers']['ninthquestionhex'] = ret[1]
    data['correct_answers']['ninthquestionbinary'] = ret[2]

    #open file HW1/output.txt
    nums = open("../../HW1/output.txt", "r")
    #choose random line in file
    #It will choose a signed/unsigned char/short where signed value range is from -128 to 255 and unsigned value range is from 0 to 255
    line = random.choice(nums.readlines())
    data['params']['nums4'] = line
    #calc nums to put in answer
    ret = convert(line)
    data['correct_answers']['tenthquestiondecimal'] = ret[0]
    data['correct_answers']['tenthquestionhex'] = ret[1]
    data['correct_answers']['tenthquestionbinary'] = ret[2]

    #open file HW1/output.txt
    nums = open("../../HW1/output.txt", "r")
    #choose random line in file
    #It will choose a signed/unsigned char/short where signed value range is from -128 to 255 and unsigned value range is from 0 to 255
    line = random.choice(nums.readlines())
    data['params']['nums5'] = line
    #calc nums to put in answer
    ret = convert(line)
    data['correct_answers']['eleventhquestiondecimal'] = ret[0]
    data['correct_answers']['eleventhquestionhex'] = ret[1]
    data['correct_answers']['eleventhquestionbinary'] = ret[2]


if __name__ == "__main__":
    generate(None)