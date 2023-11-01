from BoardPainter import *
from Reader import *
class Board:
    def __init__(self):
        self.board = [[' ' for i in range(8)] for j in range(8)]
        self.boardInit()

    def boardInit(self, path = "initBoard.txt"):
        try:
            self.board = Reader(self, path).get()
        except:
            print(f"ERROR: \'{path}\' file is lacking")

    def __getitem__(self, ind = "1a"):
        ind = self._getIndex(ind)

        return self.board[ind[0]][ind[1]]
    
    def __setitem__(self, ind = "1a", val = None):
        ind = self._getIndex(ind)

        self.board[ind[0]][ind[1]] = val

    def _getIndex(self, ind = '1a'):
        if type(ind) != str or len(ind) != 2:
            raise KeyError("Invalid board index")
        x = ord(ind[0]) - ord('1')
        y = ord(ind[1]) - ord('a')
        if x < 0 or x > 7 or y < 0 or y > 7:
            raise KeyError("Out of edges")
        return x, y 
    
    def __iter__(self):
        self.ind = 0
        return self
    
    def __next__(self):
        if self.ind == len(self.board):
            raise StopIteration
        self.ind += 1
        return self.board[self.ind - 1]

    def __str__(self):
        return BoardPainter.colorize(self)

if __name__ == "__main__":
    board = Board()
    print(board)

    for i in range(1, 9):
        p = board[str(i) + 'a']
        if p != None:
            print(board[str(i) + 'a'], board[str(i) + 'a'].color)
        else:
            print(None)

    print(board['2a'].move('3a'))

    for i in range(1, 9):
        p = board[str(i) + 'a']
        if p != None:
            print(board[str(i) + 'a'], board[str(i) + 'a'].color)
        else:
            print(None)