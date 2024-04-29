import random, math

instructions = [
    "ADD", "SUB", "MOV", "MUL", "NEG"
]

registers = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
]

def generate(data):
    data["params"]["inst"] = random.choice(instructions)
    dst = random.sample(registers, 1)[0]
    data["params"]["dst"] = dst
    data["params"]["src"] = random.sample(registers, 1)[0]

    data["correct_answers"]["register"] = dst
    pass
