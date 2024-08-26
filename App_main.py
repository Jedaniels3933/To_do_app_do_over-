from helper import *
task_list= []

def main ():
    print("Welcome to the To-do list app - Time to get off your lazy ass and do something or you will be sorry")
    flag = True
    while flag:
        ans = input(""" 
Enter an invalid command, I dare you we will virus and malware you....hard 
Now, quit playing around and enter a numerical value only....there are 4 choices , only 4. 1,2,3,4  - pick one now!

Menu:
1. Add a task
2. View tasks
3. Delete a task
4. Quit

""")
        
        if ans == "1":
            print("\nYou have chosen to add a task")
            d()
            print("\nWe here at the amazing TO-do App would love to make a suggestion , add Touch Grass for starters..maybe take a break from the Tic Toc  ")
            d2()
            print(" \nAnd call your Mother, she misses you ")
            
            add_task()
            
        elif ans == "2":
            print("\nYou have chosen to view all tasks")
            d()
            print("\nIf you have a lot of tasks, may we suggest you actually get some of them done ")
            d2()
            display_tasks()

        elif ans == "3":
            print("\nYou have chosen to delete a task")
            print("\nAre you deleting this task because it's been completed?")
            d()
            print("\nIf you are deleting this task because you are too lazy to do it then shame on you.....shame.")
            d2()
            delete_task()
        elif ans == "4":
            print("\nLeaving already, well bye then")
            d()
            d2()
            break
        else:
            print("\nYou have chosen....poorly, please try again")

def add_task():
    task = input("\nPlease enter the task you would like to add: ")
    task_list.append(task)
    print("\nTask has been added, you better do it and be quick about it ")

def display_tasks():
    if not task_list:
        print("\nThere are no tasks to display, you have nothing to do, you must be bored.....or just plain lazy ")
    else:
        for i in range(len(task_list)):
            print(f"{i+1}. {task_list[i]}")
def delete_task():
    display_tasks()
    try:
        task = int(input("\nPlease enter the number of the task you would like to delete, you better not type in a letter or symbol, we are warning you : "))
        task_list.pop(task-1)
        print(f" Task number {task} has been deleted")
    except ValueError:
        if input != int:
            print("\nInvalid input, as a punishment for not entering a number like your were told you are banished back to the main menu")
   

main()