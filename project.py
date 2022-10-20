from os import system
import os



def elicitInt(_min, _max):
    valid = False    
    while not valid:
        _in = input(f"Enter a Valid interger between {_min} and {_max} \
            (inclusive of both): ")
        try:
            _in = int(_in)

            if _min <= _in <= _max:
                valid = True 
            else:
                print("Interger out of bounds")
        except ValueError:
            print("Invalid interger provided")
    return _in
        

def printMenu():
    print("1:) Add  2) List  3) Delete   4) Count Tasks  5)  Quit")


def acceptInput():
    return elicitInt(1, 5,)


def addTask(): pass
def ListTasks(): pass
def DeleteTasks(): pass
def countTasks(): pass   


def handleMenuInput(userInput):
    _quit = False

    if userInput == 1:
        addTask()
    elif userInput == 2:
        listTasks()
    elif userInput == 3:
        deleteTask()
    elif userInput == 4:
        countTasks()
    elif userInput == 5:
        _quit = True
    else:
        raise ValueError("Not a valid Input")
          
    return _quit



def main():
    _quit = False
    if os.name == 'posix':
        clearCommand = "clear"
    elif os.name == 'nt':
        clearCommand = "cls"
    
    system(clearCommand)

    
    while not _quit:
        printMenu()
    
        userInput = acceptInput()

        system(clearCommand)

        _quit = handleMenuInput(userInput)

    print("Bye")



if __name__ == "__main__":
    main()

