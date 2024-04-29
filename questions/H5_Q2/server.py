import random, copy

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    letters = ["A","B","C","D","E","F"]
    oneNum = random.randint(0, 4)
    twoNum = oneNum+1
    one = letters[oneNum]
    two = letters[twoNum]
    pictures = ["diagram1.png", "diagram2.png", "diagram3.png", "diagram4.png", "diagram5.png"]

    # Put these two integers into data['params']
    data['params']['one'] = one
    data['params']['two'] = two
    data['params']['picture'] = pictures[oneNum]

    # Compute the sum of these two integers
    array = [0,0,0,0,0,0]
    array[len(array)-1 - oneNum] = 1
    array[len(array)-1 - twoNum] = 1
    str1 = ""
    for x in array:
        str1 += str(x)

    # Put the sum into data['correct_answers']
    data['correct_answers']['Start'] = "SYSCTL_RCGCGPIO_R = SYSCTL_RCGCGPIO_R | 0b" + str1 + ";";
    data['correct_answers']['enable1'] = "GPIO_PORT" + one + "_DEN_R = 0xFF;"
    data['correct_answers']['enable2'] = "GPIO_PORT" + two + "_DEN_R = 0xFF;"
    data['correct_answers']['set1'] = "GPIO_PORT" + one + "_DIR_R = 0b1011_1110;"
    data['correct_answers']['set2'] = "GPIO_PORT" + two +"_DIR_R = 0b0000_1111;"
