import random, math

def generate(data):
    dst = random.randint(0, 15)
    src = random.randint(0, 15)

    data['params']['value'] = "%0.2X" % random.randint(1, 0xff)
    data["params"]["dst"] = dst
    data["params"]["src"] = src
    
    data["correct_answers"]["dst"] = dst
    data["correct_answers"]["src"] = src
    data["correct_answers"]["loaded"] = 1
