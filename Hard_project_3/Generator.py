class Generator:
    def __init__(self, filePath):
        self.filePath = filePath
        self.i = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        pass