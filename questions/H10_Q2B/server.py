import random, math

overheads = [
    10, 20, 15
]

millis = [
    10, 20, 5
]

nanos = [
    100, 200, 50, 150
]

def generate(data):
    overhead = random.choice(overheads)
    b1 = random.choice(millis)
    b2 = random.choice(nanos)
    nanos.remove(b2)
    b3 = random.choice(nanos)
    data['params']['overhead'] = overhead
    data['params']['b1'] = b1
    data['params']['b2'] = b2
    data['params']['b3'] = b3

    data['correct_answers']['b1'] = calculate(overhead, b1, 10**-3)
    data['correct_answers']['b2'] = calculate(overhead, b2, 10**-6)
    data['correct_answers']['b3'] = calculate(overhead, b3, 10**-6)

def calculate(overhead, period, scale):
    return 200 * (overhead * 10**-6) / (period * scale)
