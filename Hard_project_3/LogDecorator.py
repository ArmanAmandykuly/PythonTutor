import datetime

class LogDecorator:
    def __init__(self, func, name = None, logs = None):
        if name == None:
            name = func.__name__
        self.func = func
        self.__name__ = name
        if logs == None or type(logs) != list:
            self.logs = list()
        else:
            self.logs = logs

    def __call__(self, *args, toConsole = True, **kwds):
        begin = datetime.datetime.now()
        if toConsole:
            print(begin)
            print(self.__name__)
        res = self.func(*args, **kwds)
        end = datetime.datetime.now()
        if toConsole:
            print(end)
            print(end - begin)
        if self.logs != None:
            self.logs.append(f"Name: {self.__name__}Begin: {begin}\nEnd: {end}\nDuration: {end - begin}")
        return res

if __name__ == "__main__":
    from math import exp
    from CacheDecorator import *
    logs = []
    func = LogDecorator(print, logs = logs)
    func("Hello World")
    func(logs)
    cachedLogged = LogDecorator(CacheDecorator(exp))
    print(cachedLogged(100))
    print(cachedLogged(100))