import threading
from time import sleep, ctime

class MyThread(threading.Thread):
    def __init__(self, args, func, name=''):
        threading.Thread.__init__(self)
        self.args = args
        self.func = func
        self.name = name

    def getResult(self):
        return self.res

    def run(self):
        print('Starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())