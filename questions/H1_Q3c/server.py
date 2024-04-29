import random, copy


def generate(data):
    oneNum = random.randint(0,4)
    picturesPartTwo = ["HW1_Q3c_diagram1.jpg", "HW1_Q3c_diagram2.jpg", "HW1_Q3c_diagram3.jpg", "HW1_Q3c_diagram4.jpg", "HW1_Q3c_diagram5.jpg"]
    answers = [3, 4, 2, 3, 3]
    
    data['params']['picturesPartTwo'] = picturesPartTwo[oneNum]
    data['params']['picturesPartThree'] = "HW1_Q3c_andDiagram.png"
    data['correct_answers']['int_value'] = answers[oneNum]