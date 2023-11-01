import json

from Board import *
from Pieces.King import *
from Pieces.Piece import *
from Player import *
from AI import *
from Writer import *
from time import sleep
class Game:
    def __init__(self, *args):
        if len(args) != 2:
            self._init2(*args)
        else:
            self._init1(*args)
        
    def _init2(self, path):
        with open(path, "r") as f:
            data = json.load(f)
            self.board = Board(data['board'])
            self.player1 = Player(data['p1'])
            self.player2 = Player(data['p2'])
            self.curPlayer = Player(data['cp'])
            self.curColor = data['curColor']
            self.win = data['win']
            self.ai = data['ai']
            if self.ai:
                self.player2 = AI(self.board)


    def _init1(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.curPlayer = player1
        self.curColor = "w"
        self.win = "x"
        self.ai = isinstance(player2, AI)

    def turn(self):
        if not self.checkKing(self.curColor):
            if self.curColor == "w":
                self.win = "b"
            else:
                self.win = "w"
            
        if self.win == "w":
            print(self.board)
            print(f"White won!\nCongratz, {self.player1.name}")
            return True
        elif self.win == "b":
            print(self.board)
            print(f"Black won!\nCongratz, {self.player2.name}")
            return True
        
        if not self.ai or self.curPlayer.name != 'ai':
            print(self.board)
        inp = self.curPlayer.move()
        if inp == "save":
            self.save()
            print("Saved!")
            return False
        pos, move = inp
        if self.board[pos] == None:
            raise RuntimeError("Empty cell")
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

    def checkKing(self, color = "w"):
        for row in self.board:
            for p in row:
                if p != None and isinstance(p, King) and p.color == color:
                    return True
        return False

    def save(self):
        file = input("Name the saving: ") + ".json"
        state = {
            "p1" : self.player1.name,
            "p2" : self.player2.name,
            "cp" : self.curPlayer.name,
            "curColor" : self.curColor,
            "win" : self.win,
            "board" : Writer.write(self.board),
            "ai" : self.ai
        }
        with open(file, "w") as f:
            json.dump(state, f)
    
if __name__ == "__main__":
    game = Game(Player("troll1"), Player("troll2"))

    while True:
        game.turn()