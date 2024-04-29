import random, copy

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    count = random.randint(0,4)
    answer = ["Pikachu", "Flareon", "Jolteon", "Geodude", "Snorlax"]
    hexanswer = []
    
    for x in range(0,len(answer[count])):
        hexanswer.append(hex(ord(answer[count][x])))
    
    c = answer[count]
    
    randomint1 = random.randint(1,5)
    randomint2 = random.randint(5,8)

    # Put these two integers into data['params']
    
    data['params']['randomint1'] = randomint1
    data['params']['randomint2'] = randomint2
    data['params']['name'] = answer[count]
    data['params']['firstletter'] = hex(int(hexanswer[0][2:],16) + randomint1)[2:]
    data['params']['secondletter'] = hexanswer[1][2:]
    data['params']['thirdletter'] = hexanswer[2][2:]
    data['params']['fourthletter'] = hexanswer[3][2:]
    data['params']['fifthletter'] = hexanswer[4][2:]
    data['params']['sixthletter'] = hexanswer[5][2:]
    data['params']['seventhletter'] = hexanswer[6][2:]

    # Compute the sum of these two integers

    # Put the sum into data['correct_answers']
    data['correct_answers']['first'] = 'C'
    data['correct_answers']['second'] = 'a'
    data['correct_answers']['third'] = 't'
    data['correct_answers']['fourth'] = "0x63"
    data['correct_answers']['fifth'] = "0x68"
    data['correct_answers']['sixth'] = "0x20"
    data['correct_answers']['seventh'] = hexanswer[0]
    data['correct_answers']['eighth'] = hexanswer[1]
    data['correct_answers']['ninth'] = hexanswer[2]
    data['correct_answers']['tenth'] = hexanswer[3]
    data['correct_answers']['eleventh'] = hexanswer[4]
    data['correct_answers']['twelfth'] = hexanswer[5]
    data['correct_answers']['thirteenth'] = hexanswer[6]
    data['correct_answers']['fourteenth'] = "0x00"
    
    data['correct_answers']['full'] = "Catch %s" % (answer[count])