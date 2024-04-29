import random, math

def generate(data):
    rang = list(range(1, 9))

    data["params"]["dst"] = random.randint(0, 15)
    data["params"]["src"] = random.randint(0, 15)
    data["params"]["inc"] = random.sample(rang, 1)[0]
    data["params"]["incwrong"] = random.sample(rang, 1)[0]
