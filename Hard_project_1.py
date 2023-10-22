from random import randint, choice, shuffle

score = 0

keys = set()

ending = None

def connectPlaces(place, places, graph, height):
    if place in places:
        places.discard(place)

    stack = [place]

    while len(stack) > 0:
        edgeNum = randint(1, 3)
        if edgeNum != 2:
            edgeNum = randint(1, 3)

        curPlace = stack[-1]
        stack.pop()
        for i in range(min(edgeNum, len(places))):
            if len(places) == 0:
                break
            chosenElement = choice(list(places))
            graph[curPlace].append(chosenElement)
            graph[chosenElement].append(curPlace)
            places.discard(chosenElement)
            stack.append(chosenElement)

def quest1():
    global ending, score

    answer = show("You see three doors. \n\nBehind the first door there's an ongoing fire, behind the second one we have a lion which hasn't eaten a year and behind the last one there's an automated system which will shoot you after opening.\n Which door you are going to open to go through and find the key?(type 1, 2 or 3): ")

    if answer == '1':
        ending = 1
        return
    elif answer == '3':
        ending = 2
        return
    answer = show("Congrats! You got the \'a\' key and scored 10 points! \nPress enter to continue: ")
    keys.add('a')
    score += 20

    return True

def quest2():
    global ending, score

    answer = show("You see a strange and strict mathematician teacher, and he asks: \"What is 2 + 5 = ?\"\n Your answer: ")

    if answer != '7':
        ending = 3
    else:
        answer = show("Congrats! You got the \'b\' key and scored 10 points! \nPress enter to continue: ")
        keys.add('b')
        score += 10

        return True

def quest3():
    global ending, score

    if keys == {'a', 'b'}:
        word = choice(['ilovepython', 'data-analysis', 'programming'])
        shuffled = list(word)
        shuffle(shuffled)
        answer = show("You have found keys a and b, therefore you were able to open the chest, where you see boxes with letters written on them. The letters are " + ','.join(shuffled) + ".\nWhat is the word?: ")

        counter = 0

        while answer != word and counter < 4:
            answer = show("That's not the answer, try again: ")
            counter += 1
        
        if counter == 4:
            ending = 4
            return
        
        show("Hurray! You got the key c and scored 30 points! \nPress enter to continue: ")
        score += 30
        keys.add('c')

        return True
    else:
        answer = show("To proceed this challenge, you need keys a, b \nPress enter to continue: ")

def winning():
    global ending
    if keys == {'a', 'b', 'c'}:
        ending = 4
    else:
        show("You found the main door, but, in order to open it, you need all the keys \nPress enter to continue: ")

def show(s, needDigit = False):
    answer = input(s)
    while needDigit and not answer.isdigit():
        if answer == "exit":
            answer = input("Goodbye!")
            quit()
        answer = input("Please, type a number: ")
    return answer

def game():
    global score, ending, keys
    score = 0
    ending = None
    keys = set()
    
    places = set([i for i in range(randint(5, 8))])
    graph = [[] for i in range(len(places))]
    placeQuests = dict()
    shuffled = [i for i in range(1, len(places))]
    shuffle(shuffled)
    questinds = shuffled[:4]
    questDict = dict()
    place = 0

    connectPlaces(place , places.copy(), graph, 0)

    quests = [quest1, quest2, quest3, winning]

    for i in range(len(quests)):
        questDict[questinds[i]] = i

    for i in range(len(places)):
        if i in questinds:
            placeQuests[i] = quests[questDict[i]]

    show("Yo, welcome! \n\nYou are trapped in a castle and now you have to search\n Right now, you are in the room 0, you have check other rooms in order to win\n Press enter to continue:")

    while True:
        print("Ending is", ending)
        if place in placeQuests.keys():
            if placeQuests[place]() != None:
                placeQuests.pop(place)

        if ending == None:
            if len(keys) == 0:
                print("Right now, you have no keys")
            else:
                print("Right now, you have keys:", list(keys))
            nextPlace = int(show(f"You see doors, which lead to rooms {','.join(map(str, graph[place]))} \nWhich one will you choose? \nType {','.join(map(str, graph[place]))}: ", True))
            while nextPlace not in graph[place]:
                nextPlace = int(show("Please, type the room, which is available right now: "))
            place = nextPlace
        else:
            if ending == 1:
                print("Oh no! \nYou were covered by a fire!\n You lost. Game Over")
            elif ending == 2:
                print("Oh no! \nYou were shot by bullets!\n You lost. Game Over")
            elif ending == 3:
                print("Oh no! \nYou were force d to learn mathematics in this room and you now cannot exit the castle forever! \n Morale is that you should learn arithmetics!\n You lost. Game Over")
            elif ending == 4:
                print("Congratz! You won! \n")
            show("You scored " + str(score) + "\nType anything to exit")
            quit()

if __name__ == '__main__':
    game()