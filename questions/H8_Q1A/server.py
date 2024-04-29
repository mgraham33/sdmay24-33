import random

bit_options = [10, 12, 16, 8]
vmin_options = [0, 2, 8, 10]
vmax_options = [256, 128, 200, 100]

def generate(data):
    bits = random.choice(bit_options)
    vmin = random.choice(vmin_options)
    vmax = random.choice(vmax_options)
    resolution = (vmax - vmin) / (2**bits + 1)

    data['params']['bits'] = bits
    data['params']['vmin'] = vmin
    data['params']['vmax'] = vmax
    data['params']['answer'] = "%0.3lf" % resolution
    data['correct_answers']['resolution'] = resolution
