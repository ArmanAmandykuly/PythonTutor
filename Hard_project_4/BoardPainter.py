class BoardPainter:
    def colorizeCell(cell, color = "ww"):
        if color == "ww":
            return "\x1b[1;31;47m" + cell.type
        if color == "wb":
            return "\x1b[1;31;40m" + cell.type
        if color == "bw":
            return "\x1b[1;34;47m" + cell.type
        if color == "bb":
            return "\x1b[1;34;40m" + cell.type
        if color[1] == "w":
            return "\x1b[1;31;47m "
        return "\x1b[1;31;40m " 

    def colorize(board):
        colored = list()
        for i, row in enumerate(board):
            newRow = []
            for j, cell in enumerate(row):
                bg = "w"
                c = "."
                if cell != None:
                    c = cell.color
                if ((i + j) & 1):
                    bg = "b"
                newRow.append(BoardPainter.colorizeCell(cell, c + bg))
            colored.append(newRow)
        colored.reverse()

        return "\n".join(map(lambda x: chr(ord('8') - x[0]) + "".join(x[1]) + "\x1b[0;37;40m", enumerate(colored))) + "\x1b[1;37;40m" + "\n abcdefgh"