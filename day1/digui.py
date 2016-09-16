# # def fact(n):
# #     if n == 1:
# #         return 1
# #     return n * fact(n - 1)
# #
# # #print(fact(1000))
# #
# # def fact2(n):
# #     return fact_iter(n, 1)
# #
# # def fact_iter(num, product):
# #     if num == 1:
# #         return product
# #     return fact_iter(num - 1, product * num)
# #
# # print(fact2(10))
# #
# #
# # #`递归函数,汉诺塔的移动
# # def move(n, a, b, c):
# #     if n == 1:
# #         print('move', a, '-->', c)
# #         return
# #     move(n-1, a, c, b)
# #     print('move', a, '-->', c)
# #     move(n-1, b, a, c)
# #
# # move(4, 'A', 'B', 'C')
# #
# #
# # L = []
# # n = 1
# # while n <= 99:
# #     L.append(n)
# #     n = n + 2
# # print(L)
#
# L = ['Micheal', 'Bob', 'Tracy', 'Tom', 'Nancy']
# print(L[0], L[1], L[2])
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
# print(r)
#
# print(L[0:3])
# print(L[:3])
# print(L[1:3])
# print(L[-2:])
# print(L[-2:-1])

# L = list(range(100))
# print(L[::5])
#
# T = (1, 2, 3, 4, 5)
# print(T[:3])
#
# str = 'abcdefg'
# print(str[:5])


# d = {'Li': 90, 'Bob': 80, 'Tom': 70}
# for key in d:
#     print(key)
#
# for v in d.values():
#     print(v)
#
# for k, v in d.items():
#     print(k,'-->',v)
#
# for ch in 'ABC':
#   print(ch)

# from collections import Iterable
# re = isinstance ('abc', Iterable)
# print(re)
# re2 = isinstance([1, 2, 3], Iterable)
# print(re2)
# re3 = isinstance(123, Iterable)
# print(re3)
#
# for i,value in enumerate(['A', 'B', 'C']):
#     print(i, '-->', value)
#
# for x,y in [(1, 2), (1, 3), (1, 4)]:
#     print(x,y)
#
# print(list(range(1, 11)))
#
# L = []
# for x in range(1, 11):
#     L.append(x * x)
# print(L)
#
# print([x * x for x in range(1, 11)])
#
# print([x * x for x in range(1, 11) if x % 2 == 0])
#
# print([m + n for m in 'ABC' for n in 'XYZ'])
#
# import os
# print([d for d in os.listdir('.')])

# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k,v in d.items():
#     print(k, '=', v)
# print([k + '=' + v for k, v in d.items()])
#
# L = ['HELLO', 'WORLD', 'IBM']
# print([s.lower() for s in L])

# L = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L if isinstance(s, str)]
# print(L2)

# g = (x * x for x in range(10))
# for n in g:
#     print(n)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# f = fib(6)
# for n in f:
#     print(n)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield(5)
#
# p = odd()
# print(next(p))
# print(next(p))
# print(next(p))
#
#
# g = fib(6)
# while 1:
#     try:
#         x = next(g)
#         print('g: ', x)
#     except StopIteration as e:
#         print('Generator return value: ', e.value)
#         break


###    杨辉三角
###
# def tmp(l):
#     ret=[]
#     a,b=[0]+l,l+[0]
#     for i in range(len(a)):
#         ret.append(a[i]+b[i])
#     return ret
#
# def triangles(line):
#     i,a=1,[1]
#     while i <= line:
#         yield (a)
#         a=tmp(a)
#         i=i+1
#     return 'done'
#
# l=triangles(11)
# for i in l:
#    print(i)

def add(x, y ,f ):
    return f(x) + f(y)

r = add(5, 6, abs)
print(r)
