import random, copy

def generate(data):
    class question:
         def __init__(self, name, correct):
            self.name = name
            self.correct = correct
    
    a1 = question("Car", "true")
    a2 = question("Parking meter","true")
    a3 = question("ATM","true")
    a4 = question("Toaster", "true")
    a5 = question("Phone", "true")
    a6 = question("Calculator", "true")
    a7 = question("Washing machine", "true")
    a8 = question("Vending machine", "true")
    a9 = question("WiFi router", "true")
    a10 = question("Printer", "true")
    i1 = question("Paper","false")
    i2 = question("Analog watch","false")
    i3 = question("Clothing","false")
    i4 = question("Shovel","false")
    i5 = question("Basketball","false")
    i6 = question("Baseball","false")
    i7 = question("Hammer","false")
    i8 = question("Screwdriver","false")
    i9 = question("Acoustic guitar","false")
    i10 = question("Board game","false")
    
    answer_pool = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
    incorrect_answer_pool = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
    
    for x in range(0,4):
        num = random.randint(0,len(answer_pool)-1)
        if x == 0:
            b1 = answer_pool[num]
        elif x == 1:
            b2 = answer_pool[num]
        elif x == 2:
            b3 = answer_pool[num]
        else:
            b4 = answer_pool[num]
        answer_pool.remove(answer_pool[num])
        
    for x in range(0,4):
        num = random.randint(0,len(incorrect_answer_pool)-1)
        if x == 0:
            b5 = incorrect_answer_pool[num]
        elif x == 1:
            b6 = incorrect_answer_pool[num]
        elif x == 2:
            b7 = incorrect_answer_pool[num]
        else:
            b8 = incorrect_answer_pool[num]
        incorrect_answer_pool.remove(incorrect_answer_pool[num])

    # Put these two integers into data['params']
    data['params']['a1'] = b1.name
    data['params']['a2'] = b2.name
    data['params']['a3'] = b3.name
    data['params']['a4'] = b4.name
    data['params']['i1'] = b5.name
    data['params']['i2'] = b6.name
    data['params']['i3'] = b7.name
    data['params']['i4'] = b8.name
    
    data['params']['a1Answer'] = b1.correct
    data['params']['a2Answer'] = b2.correct
    data['params']['a3Answer'] = b3.correct
    data['params']['a4Answer'] = b4.correct
    data['params']['i1Answer'] = b5.correct
    data['params']['i2Answer'] = b6.correct
    data['params']['i3Answer'] = b7.correct
    data['params']['i4Answer'] = b8.correct