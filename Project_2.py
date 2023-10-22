import json

FILENAME = "library.json"
REPEAT_MESSAGE = "Please, enter a valid data or command: "
PARAMS = ["title", "author", "year", "genre", "status"]
COMMANDS = ["add", "update", "pop", "search", "display", "save", "load", "rate"]

def library():
    books = []
    ratings = dict()

    def createBook(title, author, year, genre, status):
        return {
            "title" : title,
            "author" : author,
            "year" : year,
            "genre" : genre,
            "status" : status
        }
    
    def findBook(title, books = books):
        found = [(i, books[i]) for i in range(len(books)) if books[i]["title"] == title]
        if found:
            return found[0]
        return None, None

    def addBook(book, books = books):
        ind, found = findBook(book["title"])
        if found:
            return False
        books.append(book)
        return True

    def updBook(book, books = books):
        ind, foundBook = findBook(book["title"])
        if foundBook == None:
            return False
        books[ind] = book
        return True
    
    def popBook(title, books = books):
        ind, foundBook = findBook(title)
        if foundBook == None:
            return False
        books.pop(ind)
        return True

    def searchBooks(options, books = books):
        foundBooks = [book for book in books if (
            ((not 'title' in options) or book['title'].startswith(options['title'])) and
            ((not 'author' in options) or book['author'].startswith(options['author'])) and
            ((not 'year' in options) or book['year'] == options['year']) and
            ((not 'genre' in options) or book['genre'].startswith(options['genre'])) and
            ((not 'status' in options) or book['status'].startswith(options['status'])))]
        
        return sorted(foundBooks)
    
    def enter(prompt, repeat = REPEAT_MESSAGE, check = None):
        if check == True:
            check = lambda x: x.isdigit()
        if check == None:
            check = lambda x: True
        
        s = input(prompt)
        
        while not check(s):
            if s == "exit":
                input("Goodbye!\nPress enter to continue")
                quit()
            s = input(REPEAT_MESSAGE)
        
        return s
    
    def showBooks(books):
        for param in PARAMS:
            print(param, end = "\t")
        print("score")
        for book in books:
            for param in PARAMS:
                print(book[param], end = "\t")
            print(ratings["scores"][book["title"]])
    
    def save(books = books):
        lol = {"books" : books, "ratings" : ratings}
        with open(FILENAME, "w") as f:
            json.dump(lol, f)
        print("Data is saved successfully")

    def load(books = books, ratings = ratings):
        data = dict()
        with open(FILENAME, "r") as f:
            data = json.load(f)
        
        if len(data) > 0 and set(data['books'][0].keys()) != set(PARAMS):
            print("ERROR: Data is corrupted")
            return
        
        books.clear()
        books.extend(data['books'])
        ratings.clear()
        ratings["titles"] = data["ratings"]["titles"]
        ratings["scores"] = data["ratings"]["scores"] 
        
        print("Data is loaded successfully")

    def add():
        title = enter("Title: ")

        ind, foundBook = findBook(title)
        if foundBook:
            enter("ERROR: A book with the same title already exists")
            return
        
        author = enter("Author: ")
        year = enter("Year: ")
        genre = enter("Genre: ")
        status = "Not booked"
        
        isCompleted = addBook(createBook(title, author, year, genre, status))
        if isCompleted:
            print("It's done")
        else:
            print("ERROR: Unexpected error occurred")

    def update():
        title = enter("Title: ")
        ind, updatedBook = findBook(title)
        if not updatedBook:
            print("ERROR: A book with such title doesn't exist")
        else:
            popBook(updatedBook['title'])
            prompt = "Choose parameter to modify: "
            param = enter(prompt)
            while param in PARAMS:
                newValue = enter(f"The current value: {updatedBook[param]}\nEnter the new value: ")
                updatedBook[param] = newValue
                param = enter(prompt)
            updBook(updatedBook)
            print(f"Congrats! It's now \n{updatedBook}")

    def pop():
        title = enter("Title: ")
        ind, removedBook = findBook(title)
        if removedBook == None:
            print("ERROR: Book with such a title doesn't exist")
        else:
            popBook(title)
            print(f"{title} is removed")

    def search():
        prompt = "Choose parameter for filtering: "
        param = enter(prompt)
        options = {}
        while param in PARAMS:
            val = enter("Enter the value: ")
            options[param] = val
            param = enter(prompt)
        showBooks(searchBooks(options))

    def display(books = books):
        column = enter(f"Sort by {','.join(PARAMS)}, or rating: ", check = lambda x: x in PARAMS or x == "rating")
        
        if column in PARAMS:
            showBooks(sorted(books, key = lambda x: x[column]))
        else:
            showBooks(sorted(books, key = lambda x: ratings['scores'][x['title']], reverse = True))
        enter("Press enter to continue: ")

    def rate(ratings = ratings):
        title = enter("Enter the title: ")
        if title not in map(lambda x: x['title'], books):
            print("ERROR: no book with such a title")
            return
        
        score = int(enter("Rate from 1 to 5: ", check = True))
        comment = enter("Comment: ")

        if "titles" not in ratings:
            ratings["scores"] = dict()
            ratings["titles"] = dict()
        if title not in ratings["titles"]:
            ratings["titles"][title] = []
            ratings["scores"][title] = score
        else:
            rating = ratings["scores"][title]
            l = len(ratings["titles"][title])
            ratings["scores"][title] = (rating * len(rating) + score) / (len(rating) + 1)

        ratings["titles"][title].append({"score" : score, "comment" : comment})

    funcs = [add, update, pop, search, display, save, load, rate]

    commFuncs = dict()
    for i in range(len(COMMANDS)):
        commFuncs[COMMANDS[i]] = funcs[i]
    
    while True:
        query = enter(f"Choose command: \n{','.join(COMMANDS)}\n", check = lambda x: x in COMMANDS)
        commFuncs[query]()

if __name__ == "__main__":
    library()