import time as t

def show_menu(menu: dict):
    """Shows any menu to user"""
    for number, action in menu.items():
        print(f"{number}) {action}")

def show_local_time():
    print(t.strftime("%d %B %Y, %H:%M"))
    print()
