import random, math

def signextend(i):
    i = i & 0xff
    if (i & 0x80 == 0x80): return i | ~0xff
    return i

def generate(data):
    a0 = random.randint(1, 125)
    a1 = random.randint(1, 64)
    results = [
        [a0, random.randint(1, 127 - a0)],
        [random.randint(0, 64) - 128, -128],
        [a1, -a1],
        [random.randint(64, 100), random.randint(64, 100)]
    ]

    random.shuffle(results)

    for i in range(len(results)):
        a = results[i][0]
        b = results[i][1]
        apb_binary = (a + b) & 0xff
        apb_decimal = signextend(apb_binary)
        z = 1 if apb_decimal == 0 else 0
        c = 0 if ((a & 0xff) + (b & 0xff)) & ~0xff == 0 else 1
        n = 1 if apb_decimal < 0 else 0

        data["params"][f"a_{i}"] = a
        data["params"][f"b_{i}"] = b
        data["correct_answers"][f"a_{i}"] = a & 0xff
        data["correct_answers"][f"b_{i}"] = b & 0xff
        data["correct_answers"][f"apb_binary_{i}"] = apb_binary
        data["correct_answers"][f"apb_decimal_{i}"] = apb_decimal
        data["correct_answers"][f"z_{i}"] = z
        data["correct_answers"][f"c_{i}"] = c
        data["correct_answers"][f"n_{i}"] = n

    pass
