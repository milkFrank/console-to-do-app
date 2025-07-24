import time as t

def show_local_time():
    print(t.strftime("%d %B %Y, %H:%M"))
    print()

def show_menu(menu: dict):
    """Shows any menu to user"""
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
