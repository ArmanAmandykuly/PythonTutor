class Piece:
    def __init__(self, pos, type = "p", color = "w"):
        self.type = type
        self.color = color
        self.pos = pos

    def move(self, newPos):
        pass

    def moveCheck(self, move):
        pass
            