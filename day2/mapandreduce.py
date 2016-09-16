def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
#######

print(list(map(str, range(10))))
#######

print(list(range(10)))
#########

from functools import reduce
def fn(x,y):
    return x* 10 + y

r = reduce(fn, [1, 3, 5, 7, 9])
print(r)
#########

def add(x, y):
    return x + y

r = reduce(add, [1, 2, 3, 4])
print(r)
#########

r = sum([1,2,3,4])
print(r)
########

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}[s]

r = reduce(fn, map(char2num, '13579'))
print(r)
########

from functools import reduce

def str2int(s):
    def f1(x, y):
        return x * 10 + y
    def f2(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}[s]
    return reduce(f1, map(f2, s))
print(str2int('12345'))
#########3

def normalize(name):
    return name.capitalize()

L1 = ['NodNOD', 'kjfN', 'IJKJ']
L2 = list(map(normalize, L1))
print(L2)

def port(L):
    def ch(x, y):
        return x * y
    return reduce(ch, L)

L3 = [1, 2, 3, 4, 5]
print(port(L3))


def str2float(s):
    s = s.split('.')

    def f1(x, y):
        return x * 10 + y

    def f2(x, y):
        return x / 10 + y

    def str2num(str):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str]

    return reduce(f1, map(str2num, s[0])) + reduce(f2, list(map(str2num, s[1]))[::-1]) / 10

print(str2float('232.123'))
