import json

REPEAT_MESSAGE = "Please, enter a valid data or command: "

INGREDIENT = {
    "id" : "name",
    "columns" : ["name", "quantity", "measurement_unit"],
    "types" : [False, True, False]
}

RECIPE = {
    "id" : "title",
    "columns" : ["title", "ingredients", "cuisine"],
    "types" : [False, [INGREDIENT], False]
}

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

def ingredientInput():
    def check(s:str):
        if s == "":
            return True
        chunks = s.split()
        if len(chunks) != 4:
            return False
        if not chunks[0].isdigit():
            return False
        if chunks[-2] != 'of':
            return False
        return True
    
    s = enter(
        "Enter the data in format of \'quantity measurement of material\': ",
        check = check)
    
    if s == "":
        return None
    
    chunks = s.split()
    
    return {"name" : chunks[-1], "quantity" : int(chunks[0]), "measurement_unit" : chunks[1]}

INPUT_FUNC = {
    INGREDIENT['id'] : ingredientInput
}

def recipeManager():
    recipes = []
    
    def inputParam(dataType, name, nameGiven = False):
        if dataType == False:
            return enter(f"{name}: ")
        elif dataType == True:
            return enter(f"{name}: ", check = True)
        elif type(dataType) == list:
            s = inputParam(dataType[0], name[:-1])
            answer = []
            while s != None:
                answer.append(s)
                s = inputParam(dataType[0], name[:-1])

            return answer
        
        if dataType['id'] in INPUT_FUNC:
            return INPUT_FUNC[dataType['id']]()
        
        answer = dict()
        for name, column in zip(dataType["columns"], dataType["types"]):
            if name == dataType["id"] and nameGiven:
                answer[name] = nameGiven
                continue
            answer[name] = inputParam(column, name)
            if answer[name] == "" and column == dataType["id"]:
                return None
        
        return answer
    
    def findRecipe(name, recipes = recipes):
        for i in range(len(recipes)):
            if name == recipes[i]['title']:
                return i, recipes[i]
        return None, None
        
    def addRecipe(recipes = recipes):
        title = enter("title: ")
        if findRecipe(title)[0]:
            print("ERROR: such a recipe already exists")
            return
        
        newRecipe = inputParam(RECIPE, "recipe", title)
        recipes.append(newRecipe)

    def updRecipe(recipes = recipes):
        title = enter("title: ")
        ind, foundRecipe = findRecipe(title)

        if not foundRecipe:
            print("ERROR: No recipe with such a title")
            return

        paramToModify = enter("Choose param to modify(title, ingredients, or cuisine): ", check = lambda x: x in RECIPE['columns'])
        if paramToModify in ['title', 'cuisine']:
            recipes[ind][paramToModify] = enter(f"New {paramToModify}: ")
        else:
            command = enter("Would you like to add new or remove some?(add/pop): ", check = lambda x: x in ["add", "pop"])
            if command == "add":
                ingredient = ingredientInput()
                while ingredient:
                    recipes[ind]["ingredients"].append(ingredient)
                    ingredient = ingredientInput()
            else:
                names = list(map(lambda x: x['name'], recipes[ind]['ingredients']))
                print(','.join(names))
                name = enter("Choose an ingredient to remove: ", lambda x: x in names)
                ind = 0
                for i in range(len(names)):
                    if names[i] == name:
                        ind = i
                recipes[ind]['ingredients'].pop(ind)
                
    def popRecipe():
        title = enter("title: ")
        ind, foundRecipe = findRecipe(title)

        if not foundRecipe:
            print("ERROR: No such a recipe")
            return
        
        recipes.pop(ind)
        print("Done!")
    
    def hasIng(recipe, ingredient):
        for ing in recipe["ingredients"]:
            if ing['name'] == ingredient:
                return True
        return False

    def countIngredient(cuisine = None):
        counter = dict()
        for recipe in recipes:
            if cuisine == None or recipe['cuisine'] == cuisine:
                if not recipe['title'] in counter:
                    counter[recipe['title']] = 0
                counter[recipe['title']] += 1
        return counter

    def count():
        ing = enter("Choose ingredient: ")
        
        count = sum(map(lambda recipe: hasIng(recipe, ing), recipes))
        
        print(f"Total quantity is {count}")

    def analyse():
        cuisine = enter("Specify cuisine or just press enter")

        if not cuisine:
            cuisine = None
        
        sortedList = sorted(countIngredient().items(), key = lambda x: x[1], reverse = True)

        rowNumber = min(int(enter("How much recipes to show?: ", check = True)), len(sortedList))

        print("Recipe\tQuantity")
        for i in range(rowNumber):
            print(sortedList[i][0],'\t',sortedList[i][1])

    def ingredientAnalysis():
        command = enter("Choose to count an ingredient or show most used ingredient(count, analyse): ")
        
        if command == "analyse":
            analyse()
        elif command == "count":
            count()
        else:
            print("ERROR: No such command")

    def recipeImport(recipes = recipes):
        fileName = enter("Specify the file name: ")
        try:
            with open(fileName, "r") as f:
                data = json.load(f)

                for recipe in data:
                    if findRecipe(recipe['title']):
                        continue
                    recipes.append(recipe)
        except:
            print(f"ERROR: Failed to load {fileName}")

    def save(recipes = recipes):
        with open("recipes.json", "w") as f:
            json.dump(recipes, f)

    commands = {
        "add" : addRecipe,
        "pop" : popRecipe,
        "update" : updRecipe,
        "analysis" : ingredientAnalysis,
        "save" : save,
        "import" : recipeImport
    }

    while True:
        command = enter(f"Choose command ({','.join(commands.keys())})", check = lambda x: x in commands)
        commands[command]()
    

if __name__ == "__main__":
    recipeManager()