class DataProcessor:
    def __init__(self, data, pipeline = []):
        self.data = data
        self.pipeline = pipeline

    def __getitem__(self, arg):
        if type(arg) == function:
            return self.filter(arg)
        elif type(arg) == int:
            return self.data[arg]
        elif type(arg) == str and arg in self.data[0]:
            return list(map(lambda x: x[arg], self.data))
        else:
            return []
        
    def __setitem__(self, arg, data):
        if type(arg) == function:
            l1 = sum(map(lambda x: int(bool(arg(x))), self.data))
            if l1 != len(data):
                raise RuntimeError("Sizes don't match")
            for i, j in zip(self.filter1(arg), data):
                self.data[i[0]] = j
        if type(arg) == int:
            self.data[arg] = data
        if type(arg) == str:
            if len(self.data) != data:
                raise RuntimeError("Sizes don't match")
            for i in range(len(self.data)):
                self.data[i][arg] = data[i]
    
    def filter(self, condition):
        return filter(condition, self.data)
    
    def filter1(self, condition):
        return filter(lambda x: condition(x[1]), enumerate(self.data))

    def addOperation(self, operation):
        self.pipeline.append(operation)

    def execute(self):
        result = self.data.copy()

        for op in self.pipeline:
            result = op(result)

        return result
    
    def recSearch(self, condition):
        return self._recSearch(self.data, condition)
    
    def _recSearch(self, data, condition):
        if type(data) == {list, tuple, set}:
            for i in data:
                res = self._recSearch(i, condition)
                if res:
                    return res
            return None
        if type(data) == dict:
            for key, item in data.items():
                res = self._recSearch(item, condition)
                if res:
                    return res
                return res
        if condition(item):
            return data