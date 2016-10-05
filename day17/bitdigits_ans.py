import sys

Digit = [
    [" *** ",
    "*   *",
    "*   *",
    "*   *",
    "*   *",
    " *** "],
    [" **  ",
    " *   ",
    " *   ",
    " *   ",
    " *   ",
    " *   "]
]

try:
    digits = sys.argv[1]
    row = 0
    while row < 6:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digit[number]
            clean_digit = [logo.replace('*', str(number)) for logo in digit]
            line += clean_digit[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits_ans.py<number>")
except ValueError as err:
    print(err)