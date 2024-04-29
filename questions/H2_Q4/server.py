import random, copy, string

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    size = random.randint(1,10)
    size2 = random.randint(1,10)
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))
    res2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=size2))
    num = random.randint(1, 500)
    ch1 = random.randint(1, 300)
    ch2 = random.randint(1,200)

    # Put these two integers into data['params']
    data['params']['str1'] = res
    data['params']['str2'] = res2
    data['params']['num'] = num
    data['params']['ch1'] = ch1
    data['params']['ch2'] = ch2

    # Compute the sum of these two integers

    # Put the sum into data['correct_answers']
    data['correct_answers']['a'] = "Our {} is moving".format(res2)
    data['correct_answers']['b'] = "Read {} datasheet pages every week".format(num)
    data['correct_answers']['c'] = "CprE{}{}{} is fun!".format(chr(ch1),chr(ch2),chr(ch2))
    data['correct_answers']['d'] = "Move the {} forward for {} cm".format(res2[3:], int(num/2))
    data['correct_answers']['e'] = "The ASCII value for {} is decimal {} and hex {}".format(chr(ch1), ch1, hex(ch1))