from Player import *
from Board import *
import random
class AI(Player):
    def __init__(self, board, color = 'b'):
        super().__init__("ai")
        self.board = board
        self.color = color
    
    def move(self):
        valid = False
        validInds = []
        for i in range(8):
            for j in range(8):
                x = chr(ord('1') + i) + chr(ord('a') + j)
                if self.board[x] != None and self.board[x].color == self.color:
                    validInds.append(x)
        print(validInds)
        
        while not valid:
            randInd = random.choice(validInds)
            print(randInd)
            for i in range(8):
                for j in range(8):
                    x = chr(ord('1') + i) + chr(ord('a') + j)
                    if self.board[randInd].moveCheck(x):
                        self.board[randInd].move(x)
                        return [randInd, x]