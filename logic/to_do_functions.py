from data import data_structures as ds
from logic import menu_functions as mf

def show_to_do_list():
    """Show to-do list to user"""
    print("-- My To-Do List --")
    if ds.tasks:
        for number, task in ds.tasks.items():
            print(f"{number}) {task}")
    else:
        print("There is no tasks yet.")

def ask_task_number():
    """Ask a task number and check does it exist"""
    while True:
        task_number = mf.check_valid_number()
        if task_number not in ds.tasks.keys() and task_number != 0:
            print("---------------------------")
            print("There is no action with that number. Try again, "
                "please.")
        else:
            return task_number

def mark_task(task_number: int):
    """Mark the task as done/undone"""
    if ds.tasks[task_number][-4:] == ' [v]':
        ds.tasks[task_number] = ds.tasks[task_number][:-4]
    else:
        ds.tasks[task_number] = ds.tasks[task_number] + ' [v]'

def handle_to_do_list():
    """Do the action with to-do list depends on the user choice"""
    while True:
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
    """Add new tasks from user input"""
    while True:
        print("-- Add Tasks -- ")
        task = input("Write new task here (write «0» to go back): ")
        if task == '0':
            break
        else:
            position = len(ds.tasks) + 1 # This is the key in dict. Actually
            # it is just a number of task.
            task = task.title()
            ds.tasks[position] = task
            print(f"Task «{task}» has been added to your to-do list!\n")
