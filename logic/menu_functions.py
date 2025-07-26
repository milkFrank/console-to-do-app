import time as t
from logic import to_do_functions as tdf
from data import data_structures as ds

def greet_user():
    """Greet user by his name from the file or for the first time"""
    print(f"Hello, {ds.username}!")

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
        tdf.show_to_do_list()
