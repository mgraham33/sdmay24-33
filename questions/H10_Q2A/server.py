import random, math

duties = [25, 50, 75]
periods = [1, 5, 10, 15, 20]

def generate(data):
    period = random.choice(periods)
    duty = random.choice(duties)

    data['params']['period'] = period
    data['params']['duty'] = duty

    cycles = period * 16000
    data['params']['tbpr'] = "0x%0.2X" % (cycles >> 16)
    data['params']['tbilr'] = "0x%0.4X" % (cycles & 0xffff)

    cycles = int(cycles * (duty / 100.0))
    data['params']['tbpmr'] = "0x%0.2X" % (cycles >> 16)
    data['params']['tbmatchr'] = "0x%0.4X" % (cycles & 0xffff)
