from BoardPainter import *
class Board:
    def __init__(self):
        self.board = [[' ' for i in range(8)] for j in range(8)]
        self.boardInit()

    def boardInit(self, path = "initBoard.txt"):
        try:
            with open(path, "r") as f:
                for i, row in enumerate(f):
                    self.board[i] = row.split()
        except:
            print(f"ERROR: \'{path}\' file is lacking")

    def __getitem__(self, ind):
        x = ind[0]
        return self.board[ind]

    def __str__(self):
        return BoardPainter.colorize(self)

if __name__ == "__main__":
    board = Board()
    print(board)