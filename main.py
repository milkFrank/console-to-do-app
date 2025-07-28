from data import data_structures as ds, file_functions as ff
from logic import menu_functions as mf

while True:
    print("-- To-do App --")
    mf.show_local_time()
    mf.greet_user()
    print()
    mf.show_menu(ds.main_menu)
    menu_number = mf.ask_menu_number(ds.main_menu)
    print()
    if not menu_number: # If user chooses «exit»
        ff.write_file_tasks()
        break
    else:
        mf.handle_menu_number(menu_number)
    print("\n")
