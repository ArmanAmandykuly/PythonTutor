from BoardPainter import *
class Board:
    def __init__(self):
        self.board = [[' ' for i in range(8)] for j in range(8)]
        self.boardInit()

    def boardInit(self, path = "initBoard.txt"):
        try:
            with open(path, "r") as f:
                for i, row in enumerate(f):
                    print(row)
                    self.board[i] = row.split()
        except:
            print(f"ERROR: \'{path}\' file is lacking")

    def __getitem__(self, ind = "1a"):
        x = ord(ind[0]) - ord('1')
        y = ord(ind[1]) - ord('a')
        return self.board[x][y]
    
    def __iter__(self):
        self.ind = 0
        return self
    
    def __next__(self):
        if self.ind == len(self.board):
            raise StopIteration
        return board.board[self.ind]

    def __str__(self):
        return BoardPainter.colorize(self)

if __name__ == "__main__":
    board = Board()
    print(board)