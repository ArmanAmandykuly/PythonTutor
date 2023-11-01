class Player:
    def __init__(self, name):
        self.name = name

    def move(self):
        inp = input("Enter current position and next position: ").split()

        if inp != '' and inp[0] == "save":
            return "save"
        while not self.validPos(inp):
            inp = input("Please, input valid ones: ").split()
            if inp[0] == "save":
                return "save"
        return inp

    def validPos(self, inp):
        if inp == []:
            return False
        if len(inp) != 2:
            return False
        if len(inp[0]) != 2 or len(inp[1]) != 2:
            print(1)
            return False
        if ord(inp[0][0]) > ord('8') or ord(inp[0][1]) < ord('1'):
            print(2)
            return False
        if ord(inp[1][0]) > ord('h') or ord(inp[1][1]) < ord('a'):
            print(3)
            return False
        return True