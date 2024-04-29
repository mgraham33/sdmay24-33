import random
import math

address_space = []


def generate(data):
    char_a = random.randint(0, 0xff)
    my_coord_size = random.randint(2, 4)
    num_array_size = random.randint(2, 4)

    num_array = [random.randint(0, 0xff) for i in range(num_array_size)]

    my_coord_x = random.randint(1, my_coord_size - 1)
    my_coord_x_value = random.randint(0, 0xff)

    coord_ptr_delta = random.randint(1, my_coord_size - 1)
    coord_ptr_y_value = random.randint(0, 0xff)

    p_ptr_value0 = random.randint(0, 255)

    num_ptr_delta = random.randint(num_array_size, num_array_size + math.floor(my_coord_size / 2) - 1)
    num_ptr_value = random.randint(0x1000, 0xffff)

    p_ptr_value1 = random.randint(0xfe00, 0xffff)

    # Original homework values
    # char_a = 0x07
    # my_coord_size = 2
    # num_array_size = 2
    # num_array = [1, 4]
    # my_coord_x = 1
    # my_coord_x_value = 0x33
    # coord_ptr_delta = 1
    # coord_ptr_y_value = 0x44
    # p_ptr_value0 = 9
    # num_ptr_delta = 2
    # num_ptr_value = 0x5040
    # p_ptr_value1 = 0xfec0

    num_array_string = f'{{{", ".join([str(i) for i in num_array])}}}'
    coord_ptr_delta_string = ''
    if coord_ptr_delta == 1:
        coord_ptr_delta_string = '++'
    else:
        coord_ptr_delta_string = f' += {coord_ptr_delta}'

    data['params']['char_a'] = hex_special(char_a)
    data['params']['my_coord_size'] = my_coord_size
    data['params']['num_array_size'] = num_array_size
    data['params']['num_array'] = num_array_string
    data['params']['my_coord_x'] = my_coord_x
    data['params']['my_coord_x_value'] = hex_special(my_coord_x_value)
    data['params']['coord_ptr_delta'] = coord_ptr_delta_string
    data['params']['coord_ptr_y_value'] = hex_special(coord_ptr_y_value)
    data['params']['p_ptr_value0'] = p_ptr_value0
    data['params']['num_ptr_delta'] = num_ptr_delta
    data['params']['num_ptr_value'] = hex_special(num_ptr_value)
    data['params']['p_ptr_value1'] = hex_special(p_ptr_value1)

    #       size in bytes, used for last address value
    #     4 + 4 + 4 + 1 + (2 * my_coord_size) + (4 * num_array_size)
    address_size = 13 + (2 * my_coord_size) + (4 * num_array_size)
    start_address = 0xffffffff - (address_size - 1)

    # write coord_ptr slot
    insert_integer(p_ptr_value1) # coord_ptr assigned from *p_ptr = {value}
    # write num_ptr slot
    insert_integer(start_address + (num_ptr_delta * 4)) # num_ptr is set to effectively num_array + {value}
    # write p_ptr slot
    insert_integer(0xfffffffc) # p_ptr ends up pointing to coord_ptr
    # write char a slot
    insert_byte(char_a) # char a remains unchanged throughout the code

    # write the my_coord array
    skip_flag = False
    for i in range(my_coord_size - 1, -1, -1):
        # priority 0: if skip_flag, nothing else can be written for this byte
        if skip_flag:
            skip_flag = False
            continue
        # priority 1: if this is the values overwritten by *num_ptr = {value}, write that value
        elif i == num_ptr_delta - num_array_size + 1:
            insert_integer(num_ptr_value)
            skip_flag = True
            continue
        
        # priority 2: write the y value for this element
        if i == coord_ptr_delta:
            insert_byte(coord_ptr_y_value)
        else:
            insert_byte(0)
        
        # priority 3: write the x value for this element
        if i == my_coord_x:
            insert_byte(my_coord_x_value)
        else:
            insert_byte(0)

    # finally, write the num_array
    for i in range(num_array_size - 1, -1, -1):
        # priority 0: write value overwritten by **p_ptr = {value}
        if i == 0:
            insert_integer(p_ptr_value0)
        else:
            insert_integer(num_array[i])

    # last step is to write answers & make table
    address = 0xffffffff
    table = []
    for i in range(len(address_space)):
        data['correct_answers'][f'a{i}'] = address_space[i]
        #                   address     var name  rowspan
        table.append([hex_special(address), 0, 0])

        address -= 1

    table[0][1] = "coord_ptr"
    table[0][2] = 4
    table[4][1] = "num_ptr"
    table[4][2] = 4
    table[8][1] = "p_ptr"
    table[8][2] = 4
    table[12][1] = "a"
    table[12][2] = 1
    
    for i in range(my_coord_size):
        i0 = 13 + 2*i
        i1 = i0 + 1
        my_coord_index = my_coord_size - i - 1
        table[i0][1] = f"my_coord[{my_coord_index}].y"
        table[i0][2] = 1
        table[i1][1] = f"my_coord[{my_coord_index}].x"
        table[i1][2] = 1

    num_array_start = 13 + my_coord_size * 2
    for i in range(num_array_size):
        i0 = num_array_start + (i * 4)
        table[i0][1] = f"num_array[{num_array_size - i - 1}]"
        table[i0][2] = 4

    # finally turn the table array into actual html
    strings = []
    for i in range(len(table)):
        if (table[i][2] > 0):
            strings.append(f'<tr><td>{table[i][0]}</td><td rowspan="{table[i][2]}">{table[i][1]}</td><td><pl-integer-input answers-name="a{i}" base="16" allow-blank="true" blank-value="0" placeholder="0" label="0x"></pl-integer-input></td>')
        else:
            strings.append(f'<tr><td>{table[i][0]}</td><td><pl-integer-input answers-name="a{i}" base="16" allow-blank="true" blank-value="0" placeholder="0" label="0x"></pl-integer-input></td>')
    data['params']['table'] = '\n'.join(strings)


def insert_integer(integer):
    address_space.append((integer >> 24) & 0xff)
    address_space.append((integer >> 16) & 0xff)
    address_space.append((integer >> 8) & 0xff)
    address_space.append(integer & 0xff)


def insert_byte(byte):
    address_space.append(byte & 0xff)


def hex_special(integer):
    s = '0x' + hex(integer).upper()[2:]
    if (integer > 65535): return s[:-4] + '_' + s[-4:]
    return s
