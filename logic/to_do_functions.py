from data import menu_data as md

def show_to_do_list():
    """Show to-do list to user"""
    print("-- My To-Do List --")
    if md.tasks:
        for number, task in md.tasks.items():
            print(f"{number}) {task}")
    else:
        print("There is no tasks yet.")
