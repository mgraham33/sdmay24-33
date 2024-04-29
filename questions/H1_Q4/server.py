import random, copy, sys
sys.path.append('../../HW1')
from Hw1Q4 import sizeof, singlearray, doublearray, calculate

#Written by: Ryan Bumann

def generate(data):


    #sizeof function throughout is used to determine the size of the data type. It will return the size of the data type in bytes.

    #singlearray function throughout is used to determine the number between [] in string

    #doublearray function throughout is used to determine the product of the numbers between [][] in string


    #open file HW1/OutputsQ4/outputvar.txt
    var = open("../../HW1/OutputsQ4/outputvar.txt")
    #read random line from file
    #It will choose from unsigned: char, short, int, long, signed: char, short, int, long, and base: char, short, int, long
    line = random.choice(var.readlines())
    data['params']['firstquestion'] = line
    data['correct_answers']['firstquestion'] = sizeof(line)

    #open file HW1/OutputsQ4/outputsigarray.txt
    sigarray = open("../../HW1/OutputsQ4/outputsigarray.txt")
    #read random line from file
    #It will choose from unsigned: char, short, int, long, signed: char, short, int, long, and base: char, short, int, long. The number between [] will be from 10 to 1000
    line = random.choice(sigarray.readlines())
    data['params']['secondquestion'] = line
    data['correct_answers']['secondquestion'] = calculate(sizeof(line), singlearray(line))

    #open file HW1/OutputsQ4/outputsigarray.txt
    sigarray = open("../../HW1/OutputsQ4/outputsigarray.txt")
    #read random line from file
    #It will choose from unsigned: char, short, int, long, signed: char, short, int, long, and base: char, short, int, long. The number between [] will be from 10 to 1000
    line = random.choice(sigarray.readlines())
    data['params']['thirdquestion'] = line
    data['correct_answers']['thirdquestion'] = calculate(sizeof(line), singlearray(line))

    #open file HW1/OutputsQ4/outputsigarray.txt
    sigarray = open("../../HW1/OutputsQ4/outputsigarray.txt")
    #read random line from file
    #It will choose from unsigned: char, short, int, long, signed: char, short, int, long, and base: char, short, int, long. The number between [] will be from 10 to 1000
    line = random.choice(sigarray.readlines())
    data['params']['fourthquestion'] = line
    data['correct_answers']['fourthquestion'] = calculate(sizeof(line), singlearray(line))

    #open file HW1/OutputsQ4/outputdoubarray.txt
    douarray = open("../../HW1/OutputsQ4/outputdoubarray.txt")
    #read random line from file
    #It will choose from unsigned: char, short, int, long, signed: char, short, int, long, and base: char, short, int, long. The number between first [] will be from 10 to 100 and the number between second [] will be from 10 to 1000
    line = random.choice(douarray.readlines())
    data['params']['fifthquestion'] = line
    data['correct_answers']['fifthquestion'] = calculate(sizeof(line), doublearray(line))