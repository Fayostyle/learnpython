import random

def get_int(msg, min, default):
    while(True):
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < min:
                print("must be <=", min)
            else:
                return i
        except ValueError as err:
            print(err)

rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
min = get_int("min: (or ENTER for 0)", -100000, 0)

default = 1000
if default < min:
    default = min * 2
max = get_int("max: (or ERTER for " + str(default) + ")", min, default)

row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        num = random.randint(min, max)
        s = str(num)
        while len(s) < 10:
            s = s + " "
        line += s
        column += 1
    print(line)
    row += 1


