from data import menu_data as md, file_functions as ff
from logic import menu_functions as mf

while True:
    print("-- To-do App --")
    mf.show_local_time()
    mf.show_menu(md.main_menu)
    menu_number = mf.ask_menu_number(md.main_menu)
    print()
    if not menu_number: # If user chooses «exit»
        break
    else:
        mf.handle_menu_number(menu_number)
    print("\n")
