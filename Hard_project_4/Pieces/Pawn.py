from Piece import *
class Pawn(Piece):
    def __init__(self, pos, color = "w"):
        super().__init__(pos, "p", color)
        self.moved = False

    def move(self, newPos):
        if not self.moveCheck(newPos):
            return False
        self.pos = newPos
        self.moved = True
        return True
    
    def moveCheck(self, move):
        if self.pos[1] == '8':
            return False
        if self.pos[1] != move[1]:
            return False
        if self.moved and ord(move[0]) - ord(self.pos[0]) != 1:
            return False
        if ord(move[0]) - ord(self.pos[0]) not in [1, 2]:
            return False
        return True