import json
from data import data_structures as ds

def write_file_tasks():
    """Write tasks dictionary in the file"""
    with open('data/tasks.json', 'w') as f:
        json.dump(ds.tasks, f)

def read_file_tasks():
    """Open and read user's tasks. If there is no file — create it."""
    tasks = {}
    try:
        with open('data/tasks.json') as f:
            data = json.load(f)
            tasks = {int(key): value for key, value in data.items()} # It makes
            # key the int again, because json can't store keys as int
    except FileNotFoundError:
        return tasks
    else:
        return tasks

def write_file_name():
    """Write user's name in the file"""
    username = input("Write your name here, please: ")
    with open('data/username.txt', 'w') as f:
        f.write(username)
    print("\n")
    return username

def read_file_name():
    """Open and read user's name. If there is no name — create it."""
    username = ''
    try:
        with open('data/username.txt') as f:
            username = f.read()
    except FileNotFoundError:
        print("It seems like this is your first time opening the program!")
        username = write_file_name()
        return username
    else:
        return username.strip()
