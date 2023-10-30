class Dataset:
    def __init__(self, name, columns, data = None):
        if data == None:
            data = list()
        self.name = name
        self.columns = columns
        self.data = data
    
    def __iter__(self):
        self.iter = 0
        return self
    
    def __next__(self):
        self.iter += 1
        if self.iter == len(self.data):
            raise StopIteration
        return self.data[self.iter - 1]

def myFilter(data, condition):
    if type(data) != Dataset:
        raise TypeError("Dataset is required")
    
    return list(filter(lambda x: condition(x), data))

def myFilterDecor(condition):
    def inner(x):
        return myFilter(x, condition)
    return inner

def myMap(data, func):
    if type(data) != list:
        raise TypeError("List is required")
    
    return map(lambda x: func(x), data)

def mySum(data):
    if type(data) != list:
        raise TypeError("List is required")

    if data == []:
        return []

    res = data[0].copy()

    for key in data[0].keys():
        res[key] = sum(map(lambda x: x[key], data))
    
    return res

def myAvg(data):
    if type(data) != list:
        raise TypeError("List is required")

    if data == []:
        return []
    
    res = data[0].copy()

    for key in data[0].keys():
        res[key] = sum(map(lambda x: x[key], data)) / len(data)
    
    return res

def myExtremum(data, minRes = True):
    if type(data) != list:
        raise TypeError("List is required")

    if data == []:
        return []
    res = dict()
    for key in data[0].keys():
        if minRes:
            res[key] = min(map(lambda x:x[key], data))
        else:
            res[key] = max(map(lambda x:x[key], data))
    return res

def myMin(data):
    return myExtremum(data)

def myMax(data):
    return myExtremum(data, False)

def search(data, x):
    if data == x:
        return data
    try:
        for i in data:
            found = search(i, x)
            if found:
                return found
        return None
    except:
        return None
    
def myTimeCounter(func):
    import time
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)
    
    return inner

def myFunctionLogger(func):
    def inner(*args, **kwargs):
        print("*args:", args)
        print("**kwargs:",kwargs)
        res = func(*args, **kwargs)
        print("Returned: ", res)
    
    return inner

def generator(data):
    for chunk in data:
        yield chunk

def reduce(func, data):
    if len(data) == 1:
        return data
    res = func(data[0], data[1])
    for i in data[2:]:
        res = func(res, i)
    return res

def pipeline(functionList):
    def inner(data):
        res = data['data']
        for func in functionList:
            res = func(res)
        
        return res
    return inner

cache = dict()

def cachingDecor(func):
    def inner(dataset):
        if dataset['name'] in cache:
            return cache[dataset['name']]
        
        cache[dataset['name']] = func(dataset['data'])
        return cache[dataset['name']]
    return inner

datasets = []

def createDataset(prompt, datasets = datasets):
    tokens = prompt.split()

    if len(tokens) < 3:
        print("ERROR: Invalid format of a command")
        return
    
    newDataset = Dataset(tokens[0], tokens[1:])

    datasets.append(newDataset)

def addToDataset(tokens, datasets:list = datasets):
    if len(tokens) < 2:
        print("ERROR: Invalid format of input")
        return

    if tokens[0] in map(lambda x: x.name, datasets):
        print("ERROR: No such a dataset")
        return
    
    foundDataset = datasets[list(map(lambda x:x.name, datasets)).index(tokens[0])]

    tokens = tokens[1:]
    
    if len(tokens) != len(foundDataset.columns):
        print("ERROR: Invalid format of input")
        return
    
    row = dict()

    for i in range(len(tokens[1:])):
        try:
            row[foundDataset.columns[i]] = int(tokens[i])
        except:
            row[foundDataset.columns[i]] = tokens[i]

def popFromDataset(tokens, datasets:list = datasets):
    if len(tokens) != 2:
        print("ERROR: Invalid format of input")
        return

    if tokens[0] in map(lambda x: x.name, datasets):
        print("ERROR: No such a dataset")
        return
    
    foundDataset = datasets[list(map(lambda x:x.name, datasets)).index(tokens[0])]

    try:
        ind = int(tokens[1])
        foundDataset.pop(ind)
    except Exception:
        print("ERROR: index should be integer")
        return



commands = {
    "new" : createDataset,
    "add" : addToDataset,
    "pop" : popFromDataset,
    "remove" : removeDataset,
    "show" : show,
}

def menu():
    while True:
        command = input()
        if command == "exit":
            break

pipe = pipeline([myFilterDecor(lambda x:x['title'] == "lol"), pipeline([myFilterDecor(lambda x:x['q'] == 1)])])

print(pipe([{"title" : "lol", "q" : 1}, {"title" : "lol1", "q" : 1}, {"title" : "lol", "q" : 2}]))
# class Row:
#     def __init__(self, x:dict):
#         self.data = x
#         self.shape = len(x)
    
#     def __eq__(self, other):
#         return self.data == other.data

#     def __add__(self, other):
#         if len(self.data) != len(other.data):
#             raise RuntimeError("Different shapes")

#         res = dict()

#         for key in self.data.keys():
#             if type(self[key]) in [int, float, complex]:
#                 res[key] = self.data[key] + other.data[key]

#         return res
    
#     def __truediv__(self, n):
#         res = dict()

#         for key in self.data.keys():
#             if type(self[key]) in [int, float, complex]:
#                 res[key] = self.data[key] / n
        
#         return res