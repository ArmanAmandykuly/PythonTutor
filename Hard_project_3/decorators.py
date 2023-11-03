def logDecor(func):
    import datetime
    def inner(*args, **kwargs):
        begin = datetime.datetime.now()
        print(begin)
        print(func.__name__)
        res = func(*args, **kwargs)
        end = datetime.datetime.now()
        print(end)
        print(end - begin)
        return res
    
    return inner

def cacheDecor(func):
    memo = dict()

    def inner(*args):
        hashCode = hash(tuple(tuple(args)))
        if hashCode in memo:
            return memo[hashCode]
        memo[hashCode] = func(*args)
        return memo[hashCode]
    
    return inner

if __name__ == "__main__":
    from math import exp
    func = logDecor(print)
    func("Hello World")
    cachedLogged = logDecor(cacheDecor(exp))
    print(cachedLogged(100))
    print(cachedLogged(100))