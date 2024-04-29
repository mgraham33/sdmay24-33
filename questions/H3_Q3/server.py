import random

def generate(data):

    a_loc = "0xFFFF_FF00"
    b_loc = "0xFFFF_FE00"
    c_ptr_loc = "0xFFFF_FD00"

    a = random.randint(5, 15)
    b = random.randint(5, 15)
    c = random.randint(5, 15)

    # part a
    code = """void main(){\n    char a = """+ str(a) +""";\n    char b = """+ str(b) +""";\n    char *c_ptr;\n    c_ptr = &a;\n    *c_ptr = """+ str(c) +""";\n    *c_ptr = b;\n    c_ptr = &b;\n    *c_ptr = a;\n}"""

    a = b
    c_ptr = b_loc

    data['correct_answers']['1a'] = str(a)
    data['correct_answers']['1b'] = str(b)
    data['correct_answers']['1c'] = c_ptr
    data['params']['code1'] = code

    # part b

    a = random.randint(5, 15)
    b = random.randint(5, 15)
    c = 0

    code = """void main(){\n    char a = """+ str(a) +""";\n    char b = """+ str(b) +""";\n    char *c_ptr = """+ str(c) +""";\n    c_ptr = &a;\n    c_ptr = &b;\n    (*c_ptr)++;\n    c_ptr++;\n}"""

    b += 1
    c_ptr = b_loc

    last = int(c_ptr[len(c_ptr)-1])
    last += 1
    c_ptr = b_loc[:-1]
    c_ptr = c_ptr + str(last)

    data['correct_answers']['2a'] = str(a)
    data['correct_answers']['2b'] = str(b)
    data['correct_answers']['2c'] = c_ptr
    data['params']['code2'] = code

    # part c

    a = random.randint(5, 15)
    b = random.randint(5, 15)
    c = 0
    c_ptr = b_loc

    code = """void main(){\n    int a = """+ str(a) +""";\n    int b = """+ str(b) +""";\n    int *c_ptr = """+ str(c) +""";\n    c_ptr = &b;\n    a = *c_ptr + b;\n    (*c_ptr)++;\n    c_ptr++;\n}"""

    last = int(c_ptr[len(c_ptr)-1])
    last += 4
    c_ptr = b_loc[:-1]
    c_ptr = c_ptr + str(last)
    a = b + b
    b += 1

    data['correct_answers']['3a'] = str(a)
    data['correct_answers']['3b'] = str(b)
    data['correct_answers']['3c'] = c_ptr
    data['params']['code3'] = code
