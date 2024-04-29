import random, copy

def generate(data):

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

    # Put these two integers into data['params']
    data['params']['b'] = b
    

    # Put the sum into data['correct_answers']
    data['correct_answers']['d'] = "n/a"