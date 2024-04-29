import random, math

def generate(data):
    dst = random.randint(0, 15)
    src = random.randint(0, 15)
    store = random.randint(1, 9)
    start = random.randint(0x1, 0xf) << 28

    data["params"]["dst"] = dst
    data["params"]["src"] = src
    data["params"]["store"] = store
    data["params"]["start"] = hex(start)
    
    data["correct_answers"]["addr"] = start + store
