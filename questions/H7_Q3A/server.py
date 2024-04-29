import random, math

def generate(data):
    pin = random.randint(0, 7)
    data['params']['pin'] = pin
    data['params']['mask'] = "0x%0.2X" % (1 << pin)
    data['params']['nmask'] = "0x%0.2X" % (~(1 << pin) & 0xff)