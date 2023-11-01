from .Piece import *
class King(Piece):
    def __init__(self, pos, board, color = "w"):
        super().__init__(pos, board, "k", color)

    def moveCheck(self, move):
        if not self._moveCheck(move):
            return False
        
        dis = Metric.distance(self.pos, move)

        if abs(dis[0]) > 1 or abs(dis[1]) > 1:
            return False
        
        if self.board[move] != None and self.board[move].color == self.color:
            return False
        
        return True