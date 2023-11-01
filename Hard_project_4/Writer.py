class Writer:
    def write(board):
        res = []
        for row in board:
            newRow = []
            for p in row:
                if p == None:
                    newRow.append("w.")
                else:
                    newRow.append(p.color + p.type)
            res.append(newRow)
        return res
    
if __name__ == "__main__":
    from Board import *
    board = Board()

    print(Writer.write(board))