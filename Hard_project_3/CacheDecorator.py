class CacheDecorator:
    def __init__(self, func, name = None):
        self.memo = dict()
        self.func = func
        if name == None:
            self.__name__ = func.__name__

    def __call__(self, *args):
        hashCode = hash(tuple(tuple(args)))
        if hashCode in self.memo:
            return self.memo[hashCode]
        self.memo[hashCode] = self.func(*args)
        return self.memo[hashCode]