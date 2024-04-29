import random, copy, math

def generate(data):

    a = random.randint(100, 120) * 5 #550
    b = random.randint(5, 15) * 5 #50
    c = random.randint(1, 5) / 2 #2.5
    d = random.randint(30, 90) * 5 #350
    x1 = random.randint(150, 250) #200
    
    data['params']['a'] = a
    data['params']['b'] = b
    data['params']['c'] = c
    data['params']['d'] = d
    data['params']['x1'] = x1

    # answer1
    rise = a-b
    run = c
    m = rise/run
    answer1 = (d - b) / m
    data['correct_answers']['answer1'] = str(round(answer1, 2))

    #answer2
    rise = 5
    run = 4096
    m = rise / run
    answer2 = answer1 / m
    data['correct_answers']['answer2'] = str(math.floor(answer2))

    #answer3 and answer4
    rise = 5
    run = 4096
    m = rise / run
    answer3 = m * x1
    x2 = x1 + 1
    answer4 = m * x2
    data['correct_answers']['answer3'] = str(round(answer3, 5))
    data['correct_answers']['answer4'] = str(round(answer4, 5))
