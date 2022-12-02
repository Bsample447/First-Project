from os import system
import os
import sys
import json

# Welcome to your brand new TODO list tracker, A helpful reminder program that is only mildly worse than a written list!
# Some notes for use of program, this will create a "ThingsToDo.txt" file in your home directory,
# You may edit your text file or use the program to change the list
# within the text file, False = your Task is not done, for best readability please run the program itself!



currentPage = 0
pageStep = 5
allTasks = [[]] 


def markCompleted(index):
    global allTasks
    global writeTasks
    if not allTasks[index][0]:
        allTasks[index][0] = True
    else:
        print("That task is already completed")

    
def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def CompleteTask():
    index = takeintfromuser(1,len(allTasks), "Task to mark Complete: ")
    markCompleted(index-1)

def thiswritesthefilename(user):
    return os.path.expanduser(f"~/.ThingsToDo{user}.txt")


def thiscallsthetasks(user):
    fileName = thiswritesthefilename(user)

    if not os.path.exists(fileName): return []

    toReturn = [[]]
    
    with open(fileName) as f:
        newline = f.readline()
        toReturn = json.loads(newline)
            
    print(toReturn)
    return toReturn


def writeTasks(user, tasks):
    filename = thiswritesthefilename(user)
    
    jsonString = json.dumps(tasks)
    with open(filename, "w") as f:
        f.write(jsonString)
        

def takeintfromuser(_min, _max, msg=None):
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
                print("Please keep your Input between 1-7")
        
        except ValueError:
            print("Please choose from one of the available options with a number!")
    
    return _in
        

def printMenu():
    printPage()
    print("\nHello there! Above is a list of all your Task reminders currently set!")
    print("\n1: Add a task \n2: List of current Tasks \n3: Remove a Task  \n4: see how many Tasks you have \n5: Next Page \n6: Previous Page \n7: Complete a Task \n8: Exit TODO lists ")


def Menuinputinteraction():
    return takeintfromuser(1, 8, "Select a menu item: ")

def CheckTasks():
    global allTasks
    if allTasks[0][0]:
        index = 1
        while True:
            if allTasks[index][0]:
                index += 1
            else:
                break
        temp = allTasks[index]
        allTasks[index] = allTasks[0]
        allTasks[0] = temp
        



def addTask():
    global allTasks

    task = input("Enter a task to add: ")

    allTasks.append([False,task])

def ListTasks():
    for i in allTasks:
        print(f"{i + 1}. {allTasks[i]}")

def DeleteTasks():
    toDelete = takeintfromuser(1, len(allTasks), "Specify a task to delete: ")

    del allTasks[toDelete - 1]
    

def printPage():
    global allTasks
    global currentPage
    global pageStep

    index = currentPage * pageStep
    end = (currentPage + 1) * pageStep
    if end > len(allTasks):
        end = len(allTasks) 

    for i in range(index,end):
        if allTasks[i][0]:
            print(strike(f"{i+1}) {allTasks[i][1]}"))
        else:
            print(f"{i+1}) {allTasks[i][1]}")

def nextPage():
  global currentPage 
  global pageStep
  global allTasks
  currentPage = currentPage + 1
  if currentPage * pageStep > len(allTasks):
    currentPage = 0

def previousPage():
  global currentPage
  if currentPage == 0:
    print("Already at first page!")
  else:
    currentPage = currentPage - 1    


def CountTasks():
    print(f"\nThere are {len(allTasks)} tasks left to do.")
    input("Press enter to continue...")


def whattodowithmenuinput(userInput):
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
         nextPage()
    elif userInput == 6:
        previousPage()
    elif userInput == 7:
        CompleteTask()
    elif userInput == 8:
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
    allTasks = thiscallsthetasks(user)

    _quit = False
    
    while not _quit:
          CheckTasks()
          
          ClearScreen()


          printMenu()
    
          userInput = Menuinputinteraction()

          _quit = whattodowithmenuinput(userInput)
    
    writeTasks(user, allTasks)
    
    print("Good Bye!")

if __name__ == "__main__":
    main()