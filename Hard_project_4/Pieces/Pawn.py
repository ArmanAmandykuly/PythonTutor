from .Piece import *
class Pawn(Piece):
    def __init__(self, pos, board, color = "w"):
        super().__init__(pos, board, "p", color)
        self.moved = False

    def move(self, newPos):
        if not self.moveCheck(newPos):
            raise RuntimeError("Invalid movement")
        self.moved = True
        self.board[newPos] = self
        self.board[self.pos] = None
        self.pos = newPos
    
    def moveCheck(self, move):
        if not self._moveCheck(move):
            print(1)
            return False
        
        dis = Metric.distance(move, self.pos)

        if dis in [[1, -1], [1, 1]] and self.board[move].color != self.color:
            return True

        if self.pos[1] != move[1]:
            return False
        if self.moved and ((self.color == "w" and dis[0] != 1) or (self.color == "b" and dis[0] != -1)):
            return False
        if self.color == 'w' and dis[0] not in [1, 2] or self.color == 'b' and dis[0] not in [-1, -2]:
            return False
        if self.board[move] != None:
            return False
        if not self.moved and dis[0] == 2 and self.board[Metric.move(self.pos, [1, 0])] != None:
            return False
        
        for i in range(dis[0]):
            cell = self.board[Metric.move(self.pos, [i, 0])]
            if cell != None and cell.color == self.pos:
                print(5)
                return False
            
        return True