def is_odd(n):
    return n % 2 ==0
r = list(filter(is_odd, list(range(1,10))))
print(r)
#########

def not_empty(s):
    return s and s.strip()

r1 = list(filter(not_empty, ['a', '   ', 'CC', None,]))
print(r1)
######

#构建素数序列  埃式筛法
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

##########
#自己做的, 想法很复杂,并且不知道怎样实现!!!!!!!!!!!


# from functools import reduce
# def is_palinedrome(n):
#     x = len(str(n))
#     i = 0
#     L = []
#     while  i < x:
#         L.append(n % (pow(10, i)))
#         i = i + 1
#     print(L)
# is_palinedrome(89485985)
#     n1 = reduce(lambda x, y: x * 10 + y, L)
#     if n == n1:
#         return True
#     else:
#         return False
# output = filter(is_palinedrome, range(1, 1000))
# print(list(output))

#简单做法
def is_palindrome(n):
    return n == int(str(n)[::-1])
output = filter(is_palindrome, range(1, 1000))
print(list(output))

