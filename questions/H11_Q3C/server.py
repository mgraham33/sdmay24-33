import random, math

def generate(data):
    data["params"]["r0"] = random.randint(0, 15)
    data["params"]["r1"] = random.randint(0, 15)
    data["correct_answers"]["z"] = 1
