from Board import *
from Pieces.King import *
from Pieces.Piece import *
class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.curPlayer = player1
        self.curColor = "w"
        self.win = "x"

    def turn(self):
        if not self.checkKing(self.curColor):
            self.win = self.curColor
            return True
        
        pos, move = self.curPlayer.move()
        pColor = self.board[pos].color
        if pColor != self.curColor:
            raise RuntimeError("Player cannot use pieces of this color")
        
        self.board[pos].move(move)
        if self.curPlayer == self.player1:
            self.curPlayer = self.player2
        else:
            self.curPlayer = self.player1

        if self.curColor == "w":
            self.curColor = "b"
        else:
            self.curColor = "w"
            
        return False

    def checkKing(color = "w"):
        for row in board:
            for p in row:
                if p != None and isinstance(p) == King and p.color == color:
                    return True
        return False