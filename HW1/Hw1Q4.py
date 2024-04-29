import itertools, re

def sizeof(x):
    if 'char' in x:
        return 1
    elif 'short' in x:
        return 2
    elif 'int' in x:
        return 4
    elif 'long' in x:
        return 4
    elif 'float' in x:
        return 4

#return number between [] in string
def singlearray(x):
    x = re.findall(r'\[(.*?)\]', x)
    return int(x[0])

#return multiplied value between []s in string
def doublearray(x):
    x = re.findall(r'\[(.*?)\]', x)
    return int(x[0]) * int(x[1])

def calculate(size, array):
    return size * array
    

def main():
    
    pass
    
    

    # list1 = ["unsigned", "signed", ""]
    # list2 = ["char", "short", "int", "long"]
    # #list with range 10 to 1000 incremented by 10
    # list3 = [i for i in range(10, 1000 +10, 10)]
    # list4 = [i for i in range(10, 100 + 10, 10)]


    # outputvar = list(itertools.product(list1, list2, ['apple']))
    # outputsigarray = list(itertools.product(list1, list2, ['x'], list3))
    # outputdoubarray = list(itertools.product(list1, list2, ['x'], list4, list3))

    # #Output to OutputsQ4/outputvar.txt
    # with open('OutputsQ4/outputvar.txt', 'w') as f:
    #     for item in outputvar:
    #         f.write("%s %s %s;\n" % item)

    # with open('OutputsQ4/outputsigarray.txt', 'w') as f:
    #     for item in outputsigarray:
    #         f.write("%s %s %s[%s];\n" % item)

    # with open('OutputsQ4/outputdoubarray.txt', 'w') as f:
    #     for item in outputdoubarray:
    #         f.write("%s %s %s[%s][%s];\n" % item)

if __name__ == "__main__":
    main()