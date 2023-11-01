from .Piece import *
class Horse(Piece):
    def __init__(self, pos, board, color = "w"):
        super().__init__(pos, board, "h", color)
        
    def moveCheck(self, move):
        if not self._moveCheck(move):
            return False
        
        if set(map(abs, Metric.distance(self.pos, move))) != {1, 2}:
            return False
        
        if self.board[move] != None and self.board[move].color == self.color:
            return False
        
        return True