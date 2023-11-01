from .Metric import *
class Piece:
    def __init__(self, pos, board, type = "p", color = "w"):
        self.type = type
        self.color = color
        self.pos = pos
        self.board = board

    def move(self, newPos):
        if not self.moveCheck(newPos):
            raise RuntimeError("Invalid movement")
        self.board[self.pos] = None
        self.board[newPos] = self
        self.pos = newPos

    def _moveCheck(self, move):
        if Metric.isOut(move):
            return False
        if self.pos == move:
            return False
        return True
        
    def moveCheck(self, move):
        pass
        
        return True
            