class BoardPainter:
    def colorizeCell(cell, color = "ww"):
        if cell == '.':
            return BoardPainter.colorizeCell('  ', 'w' + color[1])
        if color == "ww":
            return "\x1b[1;31;47m" + cell[1]
        if color == "wb":
            return "\x1b[1;31;40m" + cell[1]
        if color == "bw":
            return "\x1b[1;34;47m" + cell[1]
        if color == "bb":
            return "\x1b[1;34;40m" + cell[1]

    def colorize(board):
        colored = board.board.copy()
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                print(row)
                bg, c = "w", cell
                if ((i + j) & 1):
                    bg = "b"
                colored[i][j] = BoardPainter.colorizeCell(cell, c + bg)

        return "\n".join(map(lambda x: chr(ord('1') + x[0]) + "".join(x[1]) + "\x1b[0;37;40m", enumerate(colored))) + "\x1b[1;37;40m" + "\nabcdefgh"