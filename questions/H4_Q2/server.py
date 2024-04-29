import random, copy

def generate(data):

    #part a
    ports = ["A", "B", "C", "D", "E", "F"]
    port = random.choice(ports)
    data['params']['port'] = port
    den_text = 'GPIO_PORT{}_DEN_R'.format(port)
    dir_text = 'GPIO_PORT{}_DIR_R'.format(port)
    data['params']['den'] = den_text
    data['params']['dir'] = dir_text
    
    rcgc = 0
    if port == "F":
        rcgc = 0b00100000
    elif port == "E":
        rcgc = 0b00010000
    elif port == "D":
        rcgc = 0b00001000
    elif port == "C":
        rcgc = 0b00000100
    elif port == "B":
        rcgc = 0b00000010
    elif port == "A":
        rcgc = 0b00000001
    data['correct_answers']['SYSCTL_RCGCGPIO_R'] = rcgc

    # values = ["Input", "Output"]
    # first_str = random.choice(values)
    # second_str = values[1 - values.index(first_str)]
    # data['params']['wires0-3'] = first_str
    # data['params']['wires4-7'] = second_str
    # choice = 1
    # if (first_str == "Output"):
    #     choice = 0
    # if (choice == 1):
    #     data['correct_answers']['GPIO_PORT_DEN_R'] = 0b11111111
    #     data['correct_answers']['GPIO_PORT_DIR_R'] = 0b11110000
    # else:
    #     data['correct_answers']['GPIO_PORT_DEN_R'] = 0b00000000
    #     data['correct_answers']['GPIO_PORT_DIR_R'] = 0b00001111
    
    split_point = random.randint(0, 6)
    part1_end = split_point
    part2_start = split_point + 1
    part1_str = f"0-{part1_end}" if part1_end > 0 else f"{part1_end}"
    part2_str = f"{part2_start}-7" if part2_start < 7 else f"{part2_start}"
    data['params']['input'] = part1_str
    data['params']['output'] = part2_str
    GPIO_PORT_DIR_R = 0b11111111
    GPIO_PORT_DIR_R &= (1 << part2_start) - 1 if part2_start < 7 else 0
    data['correct_answers']['GPIO_PORT_DIR_R'] = GPIO_PORT_DIR_R

    # all pins are enabled
    data['correct_answers']['GPIO_PORT_DEN_R'] = 0b11111111

    #part b
    data['params']['picture1'] = "HW4Q2P1.png"
    data['params']['picture2'] = "HW4Q2P2.png"

    gpio_options_1 = [['A', '2', 'SSI0Clk'], ['A', '3', 'SSI0Fss'], ['A', '4', 'SSI0Fss'], ['A', '5', 'SSI0Tx'], ['E', '2', 'AIN1'], ['E', '3', 'AIN0']]
    gpio_options_2 = [['A', '0', 'U0Rx', 'CAN1Rx'], ['A', '1', 'U0Tx', 'CAN1Tx'], ['A', '6', 'U0Tx', 'M1PWM2'], ['A', '7', 'I2C1SDA', 'M1PWM3'], ['B', '2', 'I2C0SCL', 'T3CCP0'], ['B', '3', 'I2C0SDA', 'T3CCP1'], ['C', '0', 'TCK SWCLK', 'T4CCP0'], ['C', '1', 'TMS SWDIO', 'T4CCP1'], ['C', '2', 'TDI', 'T5CCP0'], ['C', '3', 'TDO SWO', 'T5CCP1'], ['E', '0', 'AIN3', 'U7Rx'], ['E', '1', 'AIN2', 'U7Tx']]
    gpio_options_3 = [['B', '0', 'USB0ID', 'U1Rx', 'T2CCP0'], ['B', '1', 'USB0VBUS', 'U1Tx', 'T2CCP1'], ['B', '6', 'SSI2Rx', 'M0PWM0', 'T0CCP0'], ['B', '7', 'SSI2Tx', 'M0PWM1', 'T0CCP1'], ['D', '4', 'USB0DM', 'U6Rx', 'WT4CCP0'], ['D', '5', 'USB0DP', 'U6Tx', 'WT4CCP1']]
    gpio_options_4 = [['C', '7', 'C0-', 'U3Tx', 'WT1CCP1', 'USB0PFLT'], ['D', '6', 'U2Rx', 'M0FAULT0', 'PhA0', 'WT5CCP0'], ['D', '7', 'U2Tx', 'PhB0', 'WT5CCP1', 'NMI'], ['F', '4', 'M1FAULT0', 'IDX0', 'T2CCP0', 'USB0EPEN']]
    gpio_options_5 = [['B', '4', 'AIN10', 'SSI2Clk', 'M0PWM2', 'T1CCP0', 'CAN0Rx'], ['B', '5', 'AIN11', 'SSI2Fss', 'M0PWM3', 'T1CCP1', 'CAN0Tx'], ['C', '6', 'C0+', 'U3Rx', 'PhB1', 'WT1CCP0', 'USB0EPEN'], ['F', '2', 'SSI1Clk', 'M0FAULT0', 'M1PWM6', 'T1CCP0', 'TRD0'], ['F', '3', 'SSI1Fss', 'CAN0Tx', 'M1PWM7', 'T1CCP1', 'TRCLK']]
    gpio_options_6 = [['D', '2', 'AIN5', 'SSI3Rx', 'SSI1Rx', 'M0FAULT0', 'WT3CCP0', 'USB0EPEN'], ['D', '3', 'AIN4', 'SSI3Tx', 'SSI1Tx', 'IDX0', 'WT3CCP1', 'USB0PFLT'], ['E', '4', 'AIN9', 'U5Rx', 'I2C2SCL', 'M0PWM4', 'M1PWM2', 'CAN0Rx'], ['E', '5', 'AIN8', 'U5Tx', 'I2C2SDA', 'M0PWM5', 'M1PWM3', 'CAN0Tx']]
    gpio_options_7 = [['C', '4', 'C1-', 'U4Rx', 'U1Rx', 'M0PWM6', 'IDX1', 'WT0CCP0', 'U1RTS'], ['C', '5', 'C1+', 'U4Tx', 'U1Tx', 'M0PWM7', 'PhA1', 'WT0CCP1', 'U1CTS'], ['D', '0', 'AIN7', 'SSI3Clk', 'SSI1Clk', 'I2C3SCL', 'M0PWM6', 'M1PWM0', 'WT2CCP0'], ['D', '1', 'AIN6', 'SSI3Fss', 'SSI1Fss', 'I2C3SDA', 'M0PWM7', 'M1PWM1', 'WT2CCP1'], ['F', '1', 'U1CTS', 'SSI1Tx', 'M1PWM5', 'PhB0', 'T0CCP1', 'C1o', 'TRD1']]
    gpio_options_8 = [['F', '0', 'U1RTS', 'SSI1Rx', 'CAN0Rx', 'M1PWM4', 'PhA0', 'T0CCP0', 'NMI', 'C0o']]

    gpio_datasheet = []
    gpio_datasheet.append(gpio_options_1)
    gpio_datasheet.append(gpio_options_2)
    gpio_datasheet.append(gpio_options_3)
    gpio_datasheet.append(gpio_options_4)
    gpio_datasheet.append(gpio_options_5)
    gpio_datasheet.append(gpio_options_6)
    gpio_datasheet.append(gpio_options_7)
    gpio_datasheet.append(gpio_options_8)

    rand_b1 = random.randint(0, 5)
    data['params']['b1'] = "Port " + gpio_datasheet[0][rand_b1][0] + ", wire " + gpio_datasheet[0][rand_b1][1] + " (P" + gpio_datasheet[0][rand_b1][0] + gpio_datasheet[0][rand_b1][1] + "):"
    data['correct_answers']['b1'] = gpio_datasheet[0][rand_b1][2]

    rand_b2 = random.randint(0, 11)
    data['params']['b2'] = "Port " + gpio_datasheet[1][rand_b2][0] + ", wire " + gpio_datasheet[1][rand_b2][1] + " (P" + gpio_datasheet[1][rand_b2][0] + gpio_datasheet[1][rand_b2][1] + "):"
    data['correct_answers']['b2_1'] = gpio_datasheet[1][rand_b2][2]
    data['correct_answers']['b2_2'] = gpio_datasheet[1][rand_b2][3]

    rand_b3 = random.randint(0, 5)
    data['params']['b3'] = "Port " + gpio_datasheet[2][rand_b3][0] + ", wire " + gpio_datasheet[2][rand_b3][1] + " (P" + gpio_datasheet[2][rand_b3][0] + gpio_datasheet[2][rand_b3][1] + "):"
    data['correct_answers']['b3_1'] = gpio_datasheet[2][rand_b3][2]
    data['correct_answers']['b3_2'] = gpio_datasheet[2][rand_b3][3]
    data['correct_answers']['b3_3'] = gpio_datasheet[2][rand_b3][4]

    rand_b4 = random.randint(0, 3)
    data['params']['b4'] = "Port " + gpio_datasheet[3][rand_b4][0] + ", wire " + gpio_datasheet[3][rand_b4][1] + " (P" + gpio_datasheet[3][rand_b4][0] + gpio_datasheet[3][rand_b4][1] + "):"
    data['correct_answers']['b4_1'] = gpio_datasheet[3][rand_b4][2]
    data['correct_answers']['b4_2'] = gpio_datasheet[3][rand_b4][3]
    data['correct_answers']['b4_3'] = gpio_datasheet[3][rand_b4][4]
    data['correct_answers']['b4_4'] = gpio_datasheet[3][rand_b4][5]

    rand_b5 = random.randint(0, 4)
    data['params']['b5'] = "Port " + gpio_datasheet[4][rand_b5][0] + ", wire " + gpio_datasheet[4][rand_b5][1] + " (P" + gpio_datasheet[4][rand_b5][0] + gpio_datasheet[4][rand_b5][1] + "):"
    data['correct_answers']['b5_1'] = gpio_datasheet[4][rand_b5][2]
    data['correct_answers']['b5_2'] = gpio_datasheet[4][rand_b5][3]
    data['correct_answers']['b5_3'] = gpio_datasheet[4][rand_b5][4]
    data['correct_answers']['b5_4'] = gpio_datasheet[4][rand_b5][5]
    data['correct_answers']['b5_5'] = gpio_datasheet[4][rand_b5][6]

    rand_b6 = random.randint(0, 3)
    data['params']['b6'] = "Port " + gpio_datasheet[5][rand_b6][0] + ", wire " + gpio_datasheet[5][rand_b6][1] + " (P" + gpio_datasheet[5][rand_b6][0] + gpio_datasheet[5][rand_b6][1] + "):"
    data['correct_answers']['b6_1'] = gpio_datasheet[5][rand_b6][2]
    data['correct_answers']['b6_2'] = gpio_datasheet[5][rand_b6][3]
    data['correct_answers']['b6_3'] = gpio_datasheet[5][rand_b6][4]
    data['correct_answers']['b6_4'] = gpio_datasheet[5][rand_b6][5]
    data['correct_answers']['b6_5'] = gpio_datasheet[5][rand_b6][6]
    data['correct_answers']['b6_6'] = gpio_datasheet[5][rand_b6][7]

    rand_b7 = random.randint(0, 4)
    data['params']['b7'] = "Port " + gpio_datasheet[6][rand_b7][0] + ", wire " + gpio_datasheet[6][rand_b7][1] + " (P" + gpio_datasheet[6][rand_b7][0] + gpio_datasheet[6][rand_b7][1] + "):"
    data['correct_answers']['b7_1'] = gpio_datasheet[6][rand_b7][2]
    data['correct_answers']['b7_2'] = gpio_datasheet[6][rand_b7][3]
    data['correct_answers']['b7_3'] = gpio_datasheet[6][rand_b7][4]
    data['correct_answers']['b7_4'] = gpio_datasheet[6][rand_b7][5]
    data['correct_answers']['b7_5'] = gpio_datasheet[6][rand_b7][6]
    data['correct_answers']['b7_6'] = gpio_datasheet[6][rand_b7][7]
    data['correct_answers']['b7_7'] = gpio_datasheet[6][rand_b7][8]

    data['params']['b8'] = "Port " + gpio_datasheet[7][0][0] + ", wire " + gpio_datasheet[7][0][1] + " (P" + gpio_datasheet[7][0][0] + gpio_datasheet[7][0][1] + "):"
    data['correct_answers']['b8_1'] = gpio_datasheet[7][0][2]
    data['correct_answers']['b8_2'] = gpio_datasheet[7][0][3]
    data['correct_answers']['b8_3'] = gpio_datasheet[7][0][4]
    data['correct_answers']['b8_4'] = gpio_datasheet[7][0][5]
    data['correct_answers']['b8_5'] = gpio_datasheet[7][0][6]
    data['correct_answers']['b8_6'] = gpio_datasheet[7][0][7]
    data['correct_answers']['b8_7'] = gpio_datasheet[7][0][8]
    data['correct_answers']['b8_8'] = gpio_datasheet[7][0][9]