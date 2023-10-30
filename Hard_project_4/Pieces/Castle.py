from Piece import *
class Castle(Piece):
    def __init__(self, pos, board, color = "w"):
        super().__init__(pos, board, "c", color)
    
    def moveCheck(self, move):
        if not self._moveCheck(move):
            return False
        
        dis = Metric.distance(self.pos, move)

        if dis[0] != 0 and dis[1] != 0:
            return False
        
        for x in Metric.iterate(self.pos, move):
            if self.board[x] != None and self.board[x].color == self.color:
                return False

        return True