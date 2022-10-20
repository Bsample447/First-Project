from os import system
import os
import sys


allTasks = []

def getFilename(user):
    return os.path.expanduser(f"~/.ThingsToDo.txt{user}")


def getTasks(user):
    fileName = getFilename(user)

    if not os.path.exists(fileName): return []

    toReturn = []
    
    with open(fileName) as f:
        newline = f.readline()

        while newline != "":
            toReturn += [newline.strip()]

            newline = f.readline()
            
    return toReturn


def writeTasks(user, tasks):
    filename = getFilename(user)
    
    with open(filename, "w") as f:
        for t in tasks:
            f.write(f'{t}\n')
        

def elicitInt(_min, _max, msg=None):
    if msg == None:
        msg = f"enter a valid interget between {_min} and {_max}: "
    
    valid = False  

    while not valid:
        _in = input(msg)
        
        try:
            _in = int(_in)

            if _min <= _in <= _max:
                valid = True 
            else:
                print("Please keep your Input between 1-5")
        
        except ValueError:
            print("Please choose from one of the available options with a number!")
    
    return _in
        

def printMenu():
    ListTasks()
    print("\nHello there! Above is a list of all your Task reminders currently set!")
    print("\n1: Add a task \n2: List of current Tasks \n3: Remove a Task  \n4: see how many Tasks you have \n5: Exit Task maker")


def acceptMenuInput():
    return elicitInt(1, 5, "Select a menu item: ")


def addTask():
    global allTasks

    task = input("Enter a task to add: ")

    allTasks += [task]

def ListTasks():
    for i in range(len(allTasks)):
        print(f"{i + 1}. {allTasks[i]}")

def DeleteTasks():
    toDelete = elicitInt(1, len(allTasks), "Specify a task to delete: ")

    del allTasks[toDelete - 1]

def CountTasks():
    print(f"\nThere are {len(allTasks)} tasks left to do.")
    input("Press enter to continue...")


def handleMenuInput(userInput):
    _quit = False

    if userInput == 1:
        addTask()
    elif userInput == 2:
        ListTasks()
    elif userInput == 3:
        DeleteTasks()
    elif userInput == 4:
        CountTasks()
    elif userInput == 5:
        _quit = True
    else:
        raise ValueError("Not a valid Input")
          
    return _quit

def ClearScreen():
    if os.name == 'posix':
        clearCommand = "clear"
    elif os.name == 'nt':
        clearCommand = "cls"
    
    system(clearCommand)


def main():
    if len(sys.argv) == 1:
        user = ""
    if len(sys.argv) == 2:
        user = f"_{sys.argv[1]}"

    global allTasks
    allTasks = getTasks(user)

    _quit = False
    
    while not _quit:
          ClearScreen()

          printMenu()
    
          userInput = acceptMenuInput()

          _quit = handleMenuInput(userInput)
    
    writeTasks(user, allTasks)
    
    print("Good Bye!")

if __name__ == "__main__":
    main()