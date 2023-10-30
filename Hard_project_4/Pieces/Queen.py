from Piece import *
class Queen(Piece):
    def __init__(self, pos, board, color = "w"):
        super().__init__(pos, board, "q", color)

    def moveCheck(self, move):
        if not self._moveCheck(move):
            return False
        
        dis = Metric.distance(move, self.pos)
        
        if abs(dis[0]) != abs(dis[1]) and dis[0] != 0 and dis[1] != 0:
            return False
        
        for x in Metric.iterate(self.pos, move):
            if self.board[x] != None and self.board[x].color == self.color:
                return False
        
        return True