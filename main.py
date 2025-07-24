from data import menu_data as md
from logic import menu_functions as mf

while True:
    print("-- To-do App --")
    mf.show_local_time()
    mf.show_menu(md.main_menu)
    menu_number = mf.ask_menu_number(md.main_menu)
    if not menu_number: # If user chooses «exit»
        break
