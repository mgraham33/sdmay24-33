import sys
sys.path.append("../../")

from registerConfig.register_config import *
from registerConfig.register_names import *
import random, math

bauds = [
    9600, 14400, 4800, 2400, 19200
]

def generate(data):
    # Loads the json data
    uart_rules = RegisterRuleSet(RuleSets.UART)
    # Generates a random UARTLCRH configuration
    config = uart_rules.generate(UART.LCRH)
    # Gets the list of selected options from the random configuration
    optionsList = config.get_readable_options()
    # Removes the EPS text if the parity was disabled by PEN or PEN text if enabled
    if config.options[5]:
        del optionsList[5]
    else:
        del optionsList[4]
        config.mask &= ~0x4 # EPS bit doesn't matter if PEN is disabled
    
    # Uses the optionsList to put the bulleted list frame format into the question
    data['params']['frame_format'] = optionsList
    # Puts the configured register into the parameters for sending to the grader
    data['params']['uartlcrh'] = config.register_value
    data['params']['uartlcrh_mask'] = config.mask

    data['params']['masked'] = config.mask == 0xff
    data['params']['lcrh_str'] = "0x%0.2X" % (config.register_value & config.mask)
    
    baud = random.choice(bauds)
    data['params']['baud'] = baud

    parts = divmod(16_000_000 / (16 * baud), 1)
    data['params']['ibrd'] = int(parts[0])
    data['params']['ibrd_full'] = "%0.6lf" % (parts[0] + parts[1])
    fbrd_full = parts[1] * 64 + 0.5
    data['params']['fbrd'] = int(fbrd_full)
    data['params']['fbrd_part'] = parts[1]
    data['params']['fbrd_full'] = fbrd_full

