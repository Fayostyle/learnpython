def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2016-09-06')
now()

def log2(text):
    def decorator(func):
        def wrapper2(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper2
    return decorator

@log2('excute')
def now2():
    print('i just do it nomatter it would be work or not')

now2()
print(now.__name__)
print(now2.__name__)

#一个完整的decorator写法
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)
    return wrapper

#带参数的decorator
import functools

def log2(text):
    def decorator2(func):
        @functools.wraps(func)
        def wrapper2(*args, **kw):
            print('%s %s(): '% (text, func,__name__))
            return func(*args, **kw)
        return wrapper2
    return decorator2


###############################
# 装饰器是普通的方法
def my_decorator(func):
    print ("I am a ordinary function")
    def wrapper():
        print ("I am function returned by the decorator")
        func()
    return wrapper

# 所以，你可以不通过@调用它

def lazy_function():
    print ("zzzzzzzz")

decorated_function = my_decorator(lazy_function)
#outputs: I am a ordinary function

# It outputs "I am a ordinary function", because that's just what you do:

# 调用一个函数，没有什么特别
@my_decorator
def lazy_function():
    print ("zzzzzzzz")

#outputs: I am a ordinary function