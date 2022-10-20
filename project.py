def printMenu():
    print("1:) Add  2) List  3) Delete   4) Count Tasks  5)  Quit")


def acceptInput(): pass


def handleInput(userInput):
    print("quitting")
    return True



def main():
    _quit = False
    
    while not _quit:
        printMenu()

        userInput = acceptInput()
        _quit = handleInput(userInput)



if __name__ == "__main__":
    main()

