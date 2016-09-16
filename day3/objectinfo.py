print(type(123))
print(type('dsfsdf'))
print(type(None))
print(type(abs))


class Myobject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = Myobject()

print(hasattr(obj, 'x'))
print(obj.x)
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 's', 404))
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())