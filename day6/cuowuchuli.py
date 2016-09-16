try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
except ValueError as e:
    print('ValueError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

import logging

def foo(s):
    return 1 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar(2)
    except Exception as e:
        logging.exception(e)
main()
print('END')

class FooError(ValueError):
    pass

def foo1(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
foo1('0')


def foo2(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value : %s' % s)
    return 10 / n

def bar2():
    try:
        foo2('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar2()