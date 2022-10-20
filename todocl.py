#half unsued at this time
import os
import fileinput
import os.path
from unicodedata import name


Name = input()
open(name)
usage_file = open("usage.txt", "r")
with open(User) as f:
 def main():
    try:
        print(f'Task maker\n')
        User()
        Loop()
    except FileNotFoundError:
        print('No tasks under this user.')
        Loop()
    except Exception as e:
        global usage_msg
        print(e, '\n', '\n\n', usage_msg)

def User():
    msg = "Enter your username: "
    global User
    User = input(msg)
    print(f'\nWelcome {User}.\n')

def Loop():
    end = False
    main_screen= ["Please make a selection:",
                "1: Add your task",
                "2: Remove your task",
                "3: List your tasks",
                "4: Change user",
                "5: Exit",]
    for i in main_screen
            print(i)
            global usage_msg
            while end is not True:
            match input('Task Maker: '):
            case '1':
                
            Addtask()
            case '2':
                Remove()
            case '3':
                List()
            case '4':
                User()
            case '5':
                end = True
            case '?':
                print(usage_msg)
            case _:
                print('Please make a valid selection')
                Loop()


def Addtask():
    global User
    f = open(User + ".txt", "a")
    f.write(input("Enter a new task: ") + "\n")
    f.close()

def List():
    global User
    f = open(User + ".txt", "r")
    list = f.readlines()
    f.close()
    count = 1
    print('All tasks:\n')
    for i in list:
        print(str(count) + ". " + i, end="")
        count += 1

def Remove():
    global User
    f = open(User + ".txt", "r")
    list = f.readlines()
    f.close()
    selRem = int(input('Enter the number for a task to remove: ')) - 1
    try:
        check = input(f'Are you sure you want to remove task {selRem + 1}. {list[selRem]}? (Y/n)')
        match check.lower():
            case "y":
                list.pop(selRem)
            case "yes":
                list.pop(selRem)
            case "":
                list.pop(selRem)
            case "n":
                print('Operation cancelled.')
                Loop()
            case "no":
                print('Operation cancelled.')
                Loop()
            case _:
                print('Invalid input')
                Loop()
    except:
        print('Invalid input')
    f = open(User + ".txt", "w")
    f.writelines(list)
    f.close()

if __name__ == '__main__':
    main()