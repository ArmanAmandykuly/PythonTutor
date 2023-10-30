from Piece import *
class King(Piece):
    def __init__(self, pos, color = "w"):
        super().__init__(pos, "k", color)

    def move(self, newPos):
        if not self.moveCheck(newPos):
            return False
        self.pos = newPos
        return True

    def moveCheck(self, move):
        if ord(move[0]) > '8' or ord(move[0]) < '1' or ord(move[1]) > 'h' or ord(move[1]) < 'a':
            return False
        if abs(ord(self.pos[0]) - ord(move[0])) > 1 or abs(ord(self.pos[1]) - ord(move[1])):
            return False
        return True