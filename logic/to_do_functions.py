from data import data_structures as ds

def show_to_do_list():
    """Show to-do list to user"""
    print("-- My To-Do List --")
    if ds.tasks:
        for number, task in ds.tasks.items():
            print(f"{number}) {task}")
    else:
        print("There is no tasks yet.")

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
