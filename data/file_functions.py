def read_file_tasks():
    """Open and read user's tasks. If there is no file — create it."""
    filename = 'tasks.json'
    tasks = {}
    try:
        with open('data/tasks.json') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return tasks

def read_file_name():
    """Open and read user's name. If there is no name — create it."""
    username = ''
    try:
        with open('data/username.txt') as f:
            username = f.read()
    except FileNotFoundError:
        return None
    else:
        return username.strip()
