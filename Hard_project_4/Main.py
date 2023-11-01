from Player import *
from Game import *
from AI import *

class Main:
    def __init__(self):
        self.players = dict()
        self.players['AI'] = []
    
    def createPlayer(self):
        name = input("Please, enter your name: ")
        while name == "" or name in self.players:
            name = input("Name shouldn't be empty or the name is already taken: ")
        self.players[name] = []

    def play2(self):
        p1 = input("Please, enter the name of the first player(red): ")
        while p1 not in self.players:
            p1 = input("Please, enter the name of a player that already exists: ")
        p2 = input("Please, enter the name of the second player(blue): ")
        while p2 not in self.players:
            p2 = input("Please, enter the name of a player that already exists: ")
        game = Game(Player(p1), Player(p2))
        while game.win == 'x':
            game.turn()
    
    def play1(self):
        p = input("Please, enter the name of a player(red): ")
        while p not in self.players:
            p = input("Please, enter the name of a player that alreadty exists: ")
        game = Game(Player(p), Player("AI"))
        game.player2 = AI(game.board)
        game.ai = True
        print(game.win)
        while game.win == 'x':
            try:
                game.turn()
            except Exception as e:
                print("ERROR:", e)
        if game.win == 'w':
            self.players[game.player1.name].append("win")
            self.players[game.player2.name].append("lose")

    def loadGame(self):
        path = input("Input the filepath: ")
        try:
            game = Game(path)
            while game.win == 'x':
                try:
                    game.turn()
                except Exception as e:
                    print("ERROR:", e)
                if game.win == 'w':
                    self.players[game.player1.name].append("win")
                    self.players[game.player2.name].append("lose")
        except:
            print(f"ERROR: {path} is not found")
    
    def menu(self):
        while True:
            c = input("Input the command(play1, play2, createPlayer, load)")
            if c == "play1":
                self.play1()
            elif c == "play2":
                self.play2()
            elif c == "createPlayer":
                self.createPlayer()
            elif c == "load":
                self.loadGame()

if __name__ == "__main__":
    main = Main()
    main.menu()