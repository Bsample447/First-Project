from fileinput import filename
from inspect import getfile
from lib2to3.pgen2.token import NEWLINE
from os import system
import os
from tkinter import N
from turtle import clearscreen

allTasks = []

def getFilename():
    return os.path.expanduser("~/.task-tracker-tasks")


def getTasks():
    fileName = getFilename()

    if not os.path.exists(fileName): return []

    toReturn = []
    
    with open(fileName) as f:
        newline = f.readline()

        while newline != "":
            toReturn += [newline.strip()]
            
    return toReturn


def writeTasks(tasks):
    filename = getFilename()
    
    with open(filename, "w") as f:
        for t in tasks:
            f.write(f'{t}\n')
        return f.writelines(tasks)



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
    ListTasks()
    print("\n1:) Add  2) List  3) Delete   4) Count Tasks  5)  Quit")


def acceptMenuInput():
    return elicitInt(1, 5,)



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
    print(f"\nThere are {len(allTasks)} tasks.")
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
    global allTasks
    allTasks = getTasks()

    _quit = False
    
    while not _quit:
          ClearScreen()
          printMenu()
    
          userInput = acceptMenuInput()

          _quit = handleMenuInput(userInput)
          

print("Bye")

if __name__ == "__main__":
    main()