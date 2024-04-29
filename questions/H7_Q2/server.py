import random, math, string

def generate(data):
    baudrates = [
        9600,
        14400,
        4800
    ]

    baudrate = random.choice(baudrates)
    data['params']['baudrate'] = baudrate
    data['params']['character'] = random.choice(string.ascii_letters)
    data['correct_answers']['datarate'] = baudrate * 8 / 12


