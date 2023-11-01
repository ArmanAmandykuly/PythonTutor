from Pieces.Pawn import *
from Pieces.Castle import *
from Pieces.Horse import *
from Pieces.Bishop import *
from Pieces.King import *
from Pieces.Queen import *

class Reader:
    def __init__(self, board, path = "initBoard.txt"):
        self.pieces = []
        self.typeToPiece = {
            "p" : Pawn,
            "c" : Castle,
            "h" : Horse,
            "b" : Bishop,
            "k" : King,
            "q" : Queen,
            "." : lambda *x: None
        }
        with open(path, "r") as f:
            for i, row in enumerate(f):
                self.pieces.append(self.parse(row.split(), i, board))
            self.pieces.reverse()
    
    def parse(self, row, i, board):
        return list(map(lambda x:self.typeToPiece[x[1][1]](chr(ord('8') - i) + chr(ord('a') + x[0]), board, x[1][0]), enumerate(row)))
    
    def get(self):
        return self.pieces
    
if __name__ == "__main__":
    from Board import *
    board = Board()
    reader = Reader(board)