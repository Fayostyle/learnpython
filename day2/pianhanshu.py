print(int('12345'))

print(int('12345', base=8))

print(int('12345', base=16))

def int2(x, base=8):
    return int(x, base)

print(int2('10100477374260'))

import functools
int3 = functools.partial(int, base=2)
print(int3('010101'))
print(int3('102020', base=10))