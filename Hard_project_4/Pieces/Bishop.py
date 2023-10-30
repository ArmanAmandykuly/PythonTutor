class Bishop:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def move(self, newPos):
        if not self.moveCheck(newPos):
            return False
        self.pos = newPos
        return True