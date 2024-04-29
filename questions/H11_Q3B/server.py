import random, math

def generate(data):
    data['params']['inst'] = random.choice(['MOV', 'ADD', 'SUB', 'MUL', 'AND', 'EOR', 'ORR'])
