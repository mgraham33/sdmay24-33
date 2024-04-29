import random, math, json, itertools

# If an instruction is found that isn't aligned with the 16 bit header, a programmatic way of generating this will be needed!
header16 = "<tr><th>15</th><th>14</th><th>13</th><th>12</th><th>11</th><th>10</th><th>9</th><th>8</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th><th>0</th></tr>"

answerCount = 0

class Table():
    def __init__(self, data):
        global answerCount
        dropdownOptions = {}

        for entry in data["fields"]:
            width = entry["width"]
            if width not in dropdownOptions:
                strs = itertools.product([0,1], repeat=int(width))
                if width < 5:
                    dropdownOptions[width] = ["".join(map(str, b)) for b in strs]
                else:
                    dropdownOptions[width] = ["".join(map(str, b)) for b in random.sample(list(strs), 15)]
            if entry["specific"] not in dropdownOptions[width]:
                dropdownOptions[width].append(entry["specific"])
            if entry["general"] not in dropdownOptions[width]:
                dropdownOptions[width].append(entry["general"])

        for entry in data["fields"]:
            width = entry["width"]
            options = dropdownOptions[width]
            specific_answers = [f"<pl-answer correct='{'true' if options[i] == entry['specific'] else 'false'}'>{options[i]}</pl-answer>" for i in range(len(options))]
            general_answers = [f"<pl-answer correct='{'true' if options[i] == entry['general'] else 'false'}'>{options[i]}</pl-answer>" for i in range(len(options))]
            entry["s_dropdown"] = f"<pl-dropdown answers-name='{answerCount}'>{''.join(specific_answers)}</pl-dropdown>"
            answerCount += 1
            entry["g_dropdown"] = f"<pl-dropdown answers-name='{answerCount}'>{''.join(general_answers)}</pl-dropdown>"
            answerCount += 1
        self.data = data


    def html(self, general):
        name = self.data['name'] if general else self.data['specific_name']
        title = f"<tr><th colspan='16'>{'General: ' if general else 'Specific: '}{name}</th></tr>"
        bit = 0
        data0 = []
        data1 = []
        for entry in self.data["fields"]:
            width = entry["width"]
            if general:
                s = f"<td colspan='{width}'>{entry['g_dropdown']}</td>"
            else:
                s = f"<td colspan='{width}'>{entry['s_dropdown']}</td>"
            if bit > 15:
                data1.append(s)
            else:
                data0.append(s)
            bit += width

        row1 = f"<tr class='bold_table'>{''.join(data1)}</tr>"
        row1empty = len(data1) == 0
        return f"<table class='custom_table'>{title}{header16}<tr class='bold_table'>{''.join(data0)}</tr>{'' if row1empty else header16}{'' if row1empty else row1}</table>"


def fill_entries(instructions):
    for inst in instructions:
        inst["specific_name"] = inst["name"]
        register_map = {}
        for field in inst["fields"]:
            if field["specific"] == "":
                general = field["general"]
                value = 0
                if general == "imm8":
                    value = random.randint(0, 255)
                    register_map[general] = str(value)
                else:
                    value = random.randint(0, 15)
                    register_map[general] = 'R' + str(value)
                field["specific"] = format(value, f'#0{field["width"]+2}b')[2:]
        for mapping in register_map:
            inst["specific_name"] = inst["specific_name"].replace(mapping, register_map[mapping])


def generate(data):
    with open("instructions.json", "r") as json_file:
        json_data = json.loads(json_file.read())

    instructions = random.sample(json_data, 2)
    fill_entries(instructions)
    for i in range(len(instructions)):
        t = Table(instructions[i])
        data["params"]["gtable" + str(i)] = t.html(True)
        data["params"]["stable" + str(i)] = t.html(False)
