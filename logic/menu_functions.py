import time as t
from logic import to_do_functions as tdf
from data import data_structures as ds

def greet_user():
    """Return greeting message depending on time"""
    time = int(t.strftime("%H"))
    if time >= 0 and time < 6:
        print(f"Good night, {ds.username}!")
    elif time >= 6 and time < 12:
        print(f"Good morning, {ds.username}!")
    elif time >= 12 and time < 18:
        print(f"Good afternoon, {ds.username}!")
    elif time >= 18 and time < 24:
        print(f"Good evening, {ds.username}!")

def show_local_time():
    print(t.strftime("%d %B %Y, %H:%M"))

def show_menu(menu: dict):
    """Show any menu to user"""
    for number, action in menu.items():
        print(f"{number}) {action}")

def check_valid_number():
    """Check if the number is not a str"""
    while True:
        try:
            number = int(input("\nWrite the number here: "))
        except ValueError:
            print("---------------------------")
            print("This is not a number. Try again, please.")
        else:
            return number

def ask_menu_number(menu: dict):
    """Ask a menu number and check does it exist"""
    while True:
        menu_number = check_valid_number()
        if menu_number not in menu.keys():
            print("---------------------------")
            print("There is no action with that number. Try again, "
                "please.")
        else:
            return menu_number

def handle_menu_number(menu_number: int):
    """Do the action depends on the chosen menu option"""
    if menu_number == 1:
        tdf.handle_to_do_list()
    elif menu_number == 2:
        tdf.add_tasks()
    elif menu_number == 3:
        tdf.handle_deletion_tasks()
