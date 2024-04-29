import random, copy

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    a = random.randint(-10, -5)
    short_nask = 0b11111111
    # Put these two integers into data['params']
    data['params']['a'] = a

    # Compute the sum of these two integers
    c = bin(a & short_nask).replace("0b","")
    

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c

