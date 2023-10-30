from Piece import *
class Pawn(Piece):
    def __init__(self, pos, board, color = "w"):
        super().__init__(pos, "p", color, board)
        self.moved = False

    def move(self, newPos):
        if not self.moveCheck(newPos):
            return False
        self.pos = newPos
        self.moved = True
        self.board[newPos] = self
        return True
    
    def moveCheck(self, move):
        if not self._moveCheck(move):
            return False
        
        dis = Metric.distance(move, self.pos)
        
        if self.pos[1] != move[1]:
            return False
        if self.moved and dis[0] != 1:
            return False
        if dis[0] not in [1, 2]:
            return False
        
        for i in range(dis[0]):
            cell = self.board[Metric.move(self.pos, [i, 0])]
            if cell != None and cell.color == self.pos:
                return False
            
        return True