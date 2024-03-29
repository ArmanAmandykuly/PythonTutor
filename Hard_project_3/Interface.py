from DataProcessor import *
from dataStream import *
class Interface:
    def __init__(self):
        self.datasets = {}
        self.logs = []
        self.curDataset = None
        self.commands = {
                "chooseData" : self.chooseData,
                "addData" : self.addData,
                "seeLogs" : self.seeLogs,
                "execute" : self.execute,
                "addOperation" : self.addOperation,
                "listDatasets" : self.listDatasets
            }
    
    def chooseData(self):
        name = input("Input the name of a dataset: ")
        while name not in self.datasets:
            name = input("Please, input the valid one: ")
        self.curDataset = self.datasets[name]

    def addOperation(self):
        self.curDataset.add(op)
    
    def seeLogs(self):
        print(self.logs)

    def execute(self):
        print(self.curDataset.execute())
    
    def addData(self):
        filepath = input("Enter the filepath: ")

        valid = False
        newDataset = None
        while not valid:
            try:
                with open(filepath, "r") as f:
                    valid = True
                    size = input("Specify size or just press enter")
                    if size.isdigit():
                        size = int(size)
                    else:
                        size = None
                    newDataset = DataProcessor(list(data_stream(filepath, size)))
            except:
                filepath = input("Please, check the correctned and enter again: ")
                
        name = input("Name the dataset")
        self.datasets[name] = newDataset
    
    def listDatasets(self):
        print("Datasets: ",','.join(self.datasets.keys()))
    
    def main(self):
        while True:
            command = input()
            if command not in self.commands:
                continue
            try:
                self.commands[command]()
            except Exception as e:
                print("ERROR: ", e)