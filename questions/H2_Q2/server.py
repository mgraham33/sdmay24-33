#This is an example form other homworks and does not affect the Question

import random, copy
import string

def generate(data):

    # Generate a random string with random length
    size = random.randint(1,20)
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

    # Sample two random integers between 5 and 10 (inclusive)
    m = random.randint(0,2)
    a = ["CPRE288","Math166","Econ101"]
    
    
    blist = ["CPRE","288","Math","166","Econ","101"]
    b = list(blist[m*2])
    b.append("\\0")
    for x in list(blist[(m*2)+1]):
        b.append(x)
    b.append("\\0")
       
    n = [5, 7, 10, 35, 77, 2, 3, 0, 5, 13, 23]
    
    c = random.randint(1,5)
    
    null = b.index("\\0")
    
    null1 = n.index(0)

    # New parameters
    data['params']['j'] = res
    data['params']['g'] = size - 1
    # Put these two integers into data['params']
    data['params']['a'] = a[m]
    data['params']['b'] = b
    data['params']['n'] = n
    data['params']['c'] = c
    
    # New Answers
    data['correct_answers']['k'] = size

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = len(a[m])
    
    data['correct_answers']['d'] = "n/a"
    
    data['correct_answers']['e'] = len(a[m][0:null])
    
    data['correct_answers']['f'] = 3
    
    data['correct_answers']['g'] = len(a[len(a):])
