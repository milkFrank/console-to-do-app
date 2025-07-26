def read_file():
    """Open and read user's tasks. If there is no file — create it."""
    filename = 'tasks.json'
    tasks = {}
    try:
        with open(filename) as f:
            tasks = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return tasks
