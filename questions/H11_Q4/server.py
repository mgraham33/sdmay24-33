import random, math

def generate(data):
    w = random.randint(10, 99)
    t = random.randint(10, 99)

    data["params"]["w"] = w
    data["params"]["t"] = t

    data["correct_answers"]["r1"] = (((t // 10 * 16) + (t % 10)) << 16) + ((w // 10 * 16) + (w % 10))
