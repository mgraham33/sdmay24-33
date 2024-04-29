import random, copy

def generate(data):
    #question a and answer
    a_ch = random.randint(0, 255)
    shift = random.randint(2, 10)
    data['params']['a_ch'] = hex(a_ch)
    data['params']['a_shift'] = shift
    data['correct_answers']['a_ch'] = hex((a_ch << 5) & 0xff)

    #question b and answer
    b_ch = random.randint(0, 255)
    shift = random.randint(2, 10)
    data['params']['b_ch'] = hex(b_ch)
    data['params']['b_shift'] = shift
    b_loc = "0xFFF_FFC00"
    last = int(b_loc[len(b_loc)-1])
    last = last + shift - 1
    b = b_loc[:-1]
    b = b + str(last)
    data['correct_answers']['b_short_ptr'] = b

    #question c and answer
    c = random.randint(0, 255)
    data['params']['c'] = hex(c)
    data['correct_answers']['c_my_short'] = "0x33"

    #question d and answer
    d = random.randint(-128, -120)
    data['params']['d'] = d
    d_flag = 0
    if (d != -128):
        d_flag = 1
    data['correct_answers']['d_flag'] = d_flag

    #question e and answer
    e = random.randint(0, 1)
    e_ans = 0
    if (e == 1):
        e = random.randint(1, 10)
        e_ans = 1
    data['params']['e'] = e
    data['correct_answers']['e_ch'] = e_ans