from data import file_functions as ff

main_menu = {
    1: 'Open my to-do list',
    2: 'Add tasks',
    3: 'Change tasks',
    4: 'Delete tasks',
    0: 'Exit',
    }

tasks = ff.read_file_tasks()

username = ff.read_file_name()
