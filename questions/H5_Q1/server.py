import random, copy

def generate(data):

    selector = random.randint(0, 3)
    pics = ["diagram1.png", "diagram2.png", "diagram3.png", "diagram4.png"]

    data['params']['picture'] = pics[selector]

    if (selector == 0):
        data['params']['a'] = "GPIO_PORTA_PCTL"
        data['correct_answers']['one'] = "U0RX"
        data['correct_answers']['two'] = "SSIOCLK"
        data['correct_answers']['three'] = "SSIORX"
        data['correct_answers']['four'] = "M1PWM2"
        data['correct_answers']['five'] = "0X5"
        data['correct_answers']['six'] = "0X3"
        data['correct_answers']['seven'] = "0X2"
        data['correct_answers']['eight'] = "0X0"
        data['correct_answers']['nine'] = "0X0"
        data['correct_answers']['ten'] = "0X0"
        data['correct_answers']['eleven'] = "0X1"
        data['correct_answers']['twelve'] = "0X8"

    if (selector == 1):
        data['params']['a'] = "GPIO_PORTA_AFSEL"
        data['correct_answers']['one'] = "CAN1TX"
        data['correct_answers']['two'] = "SSIOFSS"
        data['correct_answers']['three'] = "M1PWM2"
        data['correct_answers']['four'] = "I2C1SDC"
        data['correct_answers']['five'] = "1"
        data['correct_answers']['six'] = "1"
        data['correct_answers']['seven'] = "1"
        data['correct_answers']['eight'] = "0"
        data['correct_answers']['nine'] = "0"
        data['correct_answers']['ten'] = "0"
        data['correct_answers']['eleven'] = "1"
        data['correct_answers']['twelve'] = "1"

    if (selector == 2):
        data['params']['a'] = "GPIO_PORTA_PCTL"
        data['correct_answers']['one'] = "U0RX"
        data['correct_answers']['two'] = "CAN1TX"
        data['correct_answers']['three'] = "M1PWM2"
        data['correct_answers']['four'] = "I2C1SDC"
        data['correct_answers']['five'] = "0X5"
        data['correct_answers']['six'] = "0X3"
        data['correct_answers']['seven'] = "0X2"
        data['correct_answers']['eight'] = "0X0"
        data['correct_answers']['nine'] = "0X0"
        data['correct_answers']['ten'] = "0X0"
        data['correct_answers']['eleven'] = "0X1"
        data['correct_answers']['twelve'] = "0X8"

    if (selector == 3):
        data['params']['a'] = "GPIO_PORTA_AFSEL"
        data['correct_answers']['one'] = "SSIOCLK"
        data['correct_answers']['two'] = "SSIOFSS"
        data['correct_answers']['three'] = "SSIORX"
        data['correct_answers']['four'] = "I2C1SDC"
        data['correct_answers']['five'] = "1"
        data['correct_answers']['six'] = "1"
        data['correct_answers']['seven'] = "1"
        data['correct_answers']['eight'] = "0"
        data['correct_answers']['nine'] = "0"
        data['correct_answers']['ten'] = "0"
        data['correct_answers']['eleven'] = "1"
        data['correct_answers']['twelve'] = "1"