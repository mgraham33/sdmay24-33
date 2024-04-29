import random, copy

def generate(data):

    a = random.randint(1, 100)

    data['params']['a'] = a

    answer = 1/a

    data['correct_answers']['answer'] = answer
    
    b = random.randint(1, 100)

    data['params']['b'] = b

    answer2 = 1/b

    data['correct_answers']['answer2'] = answer2
    
    c = random.randint(2, 10)
    d = random.randint(2, 10)

    data['params']['c'] = c
    data['params']['d'] = d 

    answer3 = c* d * 1000

    data['correct_answers']['answer3'] = answer3

