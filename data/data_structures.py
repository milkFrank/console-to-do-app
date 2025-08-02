from data import file_functions as ff

main_menu = {
    1: 'Open my to-do list',
    2: 'Add tasks',
    3: 'Delete tasks',
    0: 'Exit',
    }

tasks = [] # Reading tasks from the file is called in main, but it stores here
# for the better approach to the list of tasks in other modules

