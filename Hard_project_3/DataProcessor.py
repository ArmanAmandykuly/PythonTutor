class DataProcessor:
    def __init__(self, data, pipeline = []):
        self.data = data
        self.pipeline = pipeline

    def addOperation(self, operation):
        self.pipeline.append(operation)

    def execute(self):
        result = self.data.copy()

        for op in self.pipeline:
            result = op(result)

        return result