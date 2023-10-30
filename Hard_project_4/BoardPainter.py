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
        for i in range(8):
            for j in range(8):
                bg, c = "w", board[i][j][0]
                if ((i + j) & 1):
                    bg = "b"
                colored[i][j] = BoardPainter.colorizeCell(board[i][j], c + bg)

        return "\n".join(map(lambda x: "".join(x) + "\x1b[0;37;40m", colored)) + "\x1b[1;37;40m"