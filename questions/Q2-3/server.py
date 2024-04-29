import string 
import random

def generate(data):

    rSize = random.randint(1, 10)

    res = ''.join(random.choices(string.ascii_letters, k=rSize))

    data['params']['h'] = res

    data['correct_answers']['g'] = rSize