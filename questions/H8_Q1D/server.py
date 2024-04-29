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

    selected = sorted(random.sample(list(ainRange), numSelected))
    voltages = [random.randint(0, 256) for _ in ainRange]
    for ain in ainRange:
        spacing = ain * 30
        drawing.append(titleText.format(spacing + 72.5, ain))
        if ain in selected:
            drawing.append(ainVector.format(spacing + 82.5))
            drawing.append(labelText.format(spacing + 70, voltages[ain]))

    data['params']['drawing'] = drawing

    selectedAIN = selected[random.randint(0, len(selected) - 1)]
    selectedVoltage = voltages[selectedAIN]
    data['params']['ain'] = selectedAIN
    data['params']['voltage'] = selectedVoltage
    data['correct_answers']['degrees'] = selectedVoltage / 2
