def read_file_tasks():
    """Open and read user's tasks. If there is no file — create it."""
    tasks = {}
    try:
        with open('data/tasks.json') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        return None
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
