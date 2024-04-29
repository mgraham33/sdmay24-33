import random

counts = [0, 0, 0, 0, 0, 0, 0]
sizes = [2, 4, 8, 1, 4, 8]
types = ["short ", "int ", "long ", "char ", "float ", "double ", "union "]
subtypes = ["signed ", "unsigned ", ""]

class Variable():
    def __init__(self):
        self.pointer = False
        self.type = -1
        self.subtype = ""
        self.size = 0
        self.array = ""

    def text(self, depth):
        ttype = types[self.type]
        pointer = ""
        if self.pointer: pointer = "*"
        string = f"{'    ' * depth}{self.subtype}{ttype}{pointer}{ttype[0] + str(counts[self.type])}{self.array};\n"
        counts[self.type] += 1
        return string


class Union(Variable):
    def __init__(self, name):
        super().__init__()
        self.type = 6
        self.variables = []
        self.name = name

    def append(self, var):
        if (var.size > self.size):
            self.size = var.size
        self.variables.append(var)

    def text(self, depth):
        texts = []
        for var in self.variables:
            texts.append(var.text(depth + 1))
        padding = '    ' * depth
        string = f"{padding}union {self.name} {{\n{''.join(texts)}{padding}}};\n"
        return string


class Struct(Variable):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.variables = []

    def append(self, var):
        self.size += var.size
        self.variables.append(var)

    def text(self):
        texts = []
        for var in self.variables:
            texts.append(var.text(1))
        return f"struct {self.name} {{\n{''.join(texts)}}};"


def generateVariable(struct):
    variable = Variable()

    selected_subtype = ""
    selected_type = random.randint(0, 5)
    if (selected_type < 3):
        selected_subtype = random.choice(subtypes)
    
    variable.size = sizes[selected_type]
    if (random.randint(0, 4) == 0):
        variable.pointer = True
        variable.size = 4
    variable.type = selected_type
    variable.subtype = selected_subtype
    struct.append(variable)

def generateUnion():
    union = Union(f"u{counts[6]}")
    counts[6] += 1
    variables = random.randint(2, 4)
    
    for _ in range(variables):
        generateVariable(union)

    return union

def generate(data):
    small_struct = Struct("small_struct")
    for _ in range(3):
        generateVariable(small_struct)
    
    small_union = Union("small_union")
    for _ in range(5):
        generateVariable(small_union)
    v = random.choice(small_union.variables)
    length = random.randint(4, 8)
    v.array = f"[{length}]"
    v.size *= length
    if (v.size > small_union.size): small_union.size = v.size
    
    medium_struct = Struct("medium_struct")
    for _ in range(2):
        generateVariable(medium_struct)
    medium_struct.append(generateUnion())

    large_struct = Struct("large_struct")
    for _ in range(4):
        generateVariable(large_struct)
    large_struct.append(generateUnion())
    large_struct.append(generateUnion())

    data['params']['code0'] = small_struct.text()
    data['correct_answers']['q0'] = small_struct.size

    data['params']['code1'] = small_union.text(0)
    data['correct_answers']['q1'] = small_union.size

    data['params']['code2'] = medium_struct.text()
    data['correct_answers']['q2'] = medium_struct.size

    data['params']['code3'] = large_struct.text()
    data['correct_answers']['q3'] = large_struct.size
