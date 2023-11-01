from .Piece import *
class Bishop(Piece):
    def __init__(self, pos, board, color = "w"):
        super().__init__(pos, board, "b", color)

    def moveCheck(self, move):
        if not self._moveCheck(move):
            return False
        
        dis = Metric.distance(self.pos, move)
        if abs(dis[0]) != abs(dis[1]):
            return False
        
        if abs(dis[0]) != abs(dis[1]):
            return False
        
        for x in Metric.iterate(x, move):
            if x != None:
                return False
        
        return True