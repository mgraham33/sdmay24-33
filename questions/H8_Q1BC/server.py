import sys
sys.path.append("../../")

from registerConfig.register_config import *
from registerConfig.register_names import *
import random, copy

titleText = '<pl-text x1="545" y1="{}" label="AIN {}" font-size="16" latex="false"></pl-text>'
ainVector = '<pl-vector x1="675" y1="{}" width="75" stroke-width="2" angle="180" color="#000000"></pl-vector>'
labelText = '<pl-text x1="680" y1="{}" label="{} V" font-size="20" latex="false"></pl-text>'

# Configure number of AINs and number of selected AINs here
numAINs = 12
numSelected = 8

ainRange = range(0, numAINs)

def generate(data):
    drawing = []

    selected = random.sample(list(ainRange), numSelected)
    voltages = [random.randint(0, 256) for _ in ainRange]
    for ain in ainRange:
        spacing = ain * 30
        drawing.append(titleText.format(spacing + 72.5, ain))
        if ain in selected:
            drawing.append(ainVector.format(spacing + 82.5))
            drawing.append(labelText.format(spacing + 70, voltages[ain]))

    data['params']['drawing'] = drawing

    # load adc rules
    adc_rules = RegisterRuleSet(RuleSets.ADC)

    # generate random adcssctl configuration
    ctl_config = adc_rules.generate(ADC.SSCTL)
    # generate random sequence length
    sequenceLen = random.randint(2, 4)
    # disable all END# bits and set SS0 as the end
    ctl_config.register_value &= 0xdddd_ddd0
    ctl_config.register_value |= 0x6
    # left shift the register to get the correct sequence length
    ctl_config.register_value <<= (4 * (sequenceLen - 1))
    # mask register to 32 bit value
    ctl_config.register_value &= 0xffff_ffff 
    # update changes to register_value into the rest of the config
    ctl_config.update_options()
    data['params']['ssctl'] = "0x%0.8X" % ctl_config.register_value

    # create a new adcssmux configuration based on the randomly selected AINs
    mux_config = RegisterConfiguration(adc_rules.get_rules(ADC.SSMUX), selected)
    data['params']['ssmux'] = "0x%0.8X" % mux_config.register_value

    data['correct_answers']['pssi'] = 1
    data['correct_answers']['ris'] = 1
    data['correct_answers']['isc'] = 1
    data['correct_answers']['seq_len0'] = sequenceLen
    data['correct_answers']['seq_len1'] = sequenceLen
    data['correct_answers']['fifo'] = "ADC0_SSFIFO0_R"

    printstr = ""
    for i in range(sequenceLen):
        printstr += str(voltages[selected[-(i + 1)]] * 4) + " "

    data['correct_answers']['print_str'] = printstr
