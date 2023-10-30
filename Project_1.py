def userMenu():
    counters = [0]

    def validate(action):
        accountNumber = request("Please, input your account number: ",
                                "Please, input a valid account number: ",
                                True)
        password = request("Please, enter the password: ")
        
        accountNumber = int(accountNumber)
        
        found = False

        for key, account in accounts.items():
            if key == accountNumber and password == account['password']:
                found = True
                return action(account)
        
        if not found:
            request("Error: No such account number exists:")
            return None

    def deposit(account):
        increase = int(request("Enter the amount to deposit: ",
                           "Enter a valid amount to deposit: ",
                           condition = lambda s: s.isdigit() and int(s) > 0))

        account['deposit'] += increase

        request(f"You have successfully deposited {increase}$ to {account['name']}\nPlease, type \"exit\" to exit or press enter in order to continue: ")

        return account, f"Deposited {increase}$ to {account['name']}"
    
    def withdraw(account):
        decrease = int(request("Enter the amount to withdraw: ", 
                           "Enter a valid amount to withdraw: ",
                           condition = lambda s: s.isdigit() and int(s) > 0 and int(s) <= account['deposit']))

        account['deposit'] -= decrease

        request(f"You have successfully withdrawed {decrease}$ from {account['name']}\nPlease, type \"exit\" to exit or press enter in order to continue: ")

        return account, f"Withdrawed {decrease}$ from {account['name']}"

    def showBalance(account):
        request(f"You have {account['deposit']}\nPlease, type \"exit\" to exit or press enter in order to continue: ")

    def history(account):
        request("\n".join(account['history']) + "\nPress enter to continue: ")
        
    def filterRequest(message):
        inputString = input(message)
        if inputString.lower() == "exit":
            print("Goodbye!")
            exit()
        
        return inputString

    def request(message, repeatMessage = "", condition = None):
        if condition == True:
            condition = lambda s: s.isdigit()

        inputString = filterRequest(message)

        if condition != None:
            while not condition(inputString):
                inputString = filterRequest(repeatMessage)

        return inputString
    
    request("Please, enter a number", "", True)
    
    def createNewAccount(counters):
        name = request("Please, input your name: ")
        if name in map(lambda x: x['name'], accounts.values()):
            request("Account with such a name already exists. \nPlease try again(press Enter): ")
            return
        
        deposit = request("Please, input your initial deposit: ",
                          "Please, input your valid initial deposit: ",
                          True)
        password = request("Please, input your password: ")

        deposit = int(deposit)

        accountNumber = counters[-1]
        counters.append(counters[-1] + 1)

        newAccount = {"name" : name, "deposit" : deposit, "password" : password, "history" : []}

        accounts[accountNumber] = newAccount

        request(f"Congratulations, {name}! \nYou have successfully created your account with number {accountNumber} \nPlease, type \"exit\" to exit or press enter in order to continue: ")

    def depositFunds():
        result = validate(deposit)
        if result == None:
            return
        
        account, transaction = result

        account['history'].append(transaction)

    def withdrawFunds():
        result = validate(withdraw)
        if result == None:
            return
        
        account, transaction = result

        account['history'].append(transaction)
    
    def checkBalance():
        validate(showBalance)

    def showHistory():
        validate(history)

    operationDict = {
        "create" : lambda: createNewAccount(counters),
        "deposit" : depositFunds,
        "withdraw" : withdrawFunds,
        "balance" : checkBalance,
        "history" : showHistory
    }

    accounts = dict()

    menuText = """
Hello! It's banking system's menu
What kind of operation you would like to proceed:

create - to create a new account
deposit - to deposit
withdraw - to withdraw
balance - to show balance
history - to show history
exit - to exit
"""
    
    while True:
        s = request(menuText, "Please, enter a valid command: ", lambda s: s in operationDict.keys())
        operationDict[s]()

if __name__ == '__main__':
    userMenu()