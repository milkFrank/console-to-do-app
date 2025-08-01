from data import data_structures as ds
from logic import menu_functions as mf

def show_to_do_list():
    """Show to-do list to user"""
    if ds.tasks:
        number = 1
        for task in ds.tasks:
            print(f"{number}) {task}")
            number += 1
    else:
        print("There is no tasks yet.")

def ask_task_number():
    """Ask a task number and check does it exist"""
    while True:
        task_number = mf.check_valid_number()
        if ((task_number < 0 or task_number > len(ds.tasks)) and
            task_number != 0):
            print("---------------------------")
            print("There is no action with that number. Try again, "
                "please.")
        else:
            return task_number

def mark_task(task_number: int):
    """Mark the task as done/undone"""
    if ds.tasks[task_number - 1][-4:] == ' [v]':
        ds.tasks[task_number - 1] = ds.tasks[task_number - 1][:-4]
    else:
        ds.tasks[task_number - 1] = ds.tasks[task_number - 1] + ' [v]'

def handle_to_do_list():
    """Do the action with to-do list depends on the user choice"""
    while True:
        print("-- My To-Do List --")
        show_to_do_list()
        if ds.tasks:
            print("\nYou can write the number of task to mark it as "
                "done/undone.")
            print("Write «0» to go back.")
            task_number = ask_task_number()
            if task_number == 0:
                break
            else:
                mark_task(task_number)
            print()
        else:
            break

def add_tasks():
    """Add new tasks from user's input"""
    while True:
        print("-- Add Tasks -- ")
        task = input("Write new task here (write «0» to go back): ")
        if task == '0':
            break
        elif task == '':
            print("You can't add empty task.\n")
        else:
            task = task.title()
            ds.tasks.append(task)
            print(f"Task «{task}» has been added to your to-do list!\n")

def delete_tasks(task_number: int):
    """Delete tasks from user's input"""
    task = ds.tasks[task_number - 1]
    del ds.tasks[task_number - 1]
    print(f"Task «{task}» has been deleted from your to-do list!")

def handle_deletion_tasks():
    while True:
        print("-- Delete Tasks --")
        show_to_do_list()
        if ds.tasks:
            print("\nYou can write the number of task to delete it.")
            print("Write «0» to go back.")
            task_number = ask_task_number()
            if task_number == 0:
                break
            else:
                delete_tasks(task_number)
            print()
        else:
            break
