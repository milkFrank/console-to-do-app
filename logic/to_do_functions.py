from data import data_structures as ds

def show_to_do_list():
    """Show to-do list to user"""
    print("-- My To-Do List --")
    if ds.tasks:
        for number, task in ds.tasks.items():
            print(f"{number}) {task}")
    else:
        print("There is no tasks yet.")
