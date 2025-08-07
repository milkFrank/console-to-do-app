# Console To-Do App
A simple CLI (Command Line Interface) app that helps users organize their work with a to-do list. 

## About the project
This project is a practical exercise, based on *Part I* of *Python Crash Course* by Eric Matthes. It demonstrates my understanding of core Python concepts, including basic syntax, CRUD operations, and the use of both built-in (*time*) and external (*unittest*, *pytest*) Python modules.

## Features
This app provides users a simple functionality for organizing their work from the command line.
- Displays the current date and time at the top of the menu
- Greets the user with their name and time-based message (e.g. «Good afternoon, Nick!»)
- Supports adding, deleting and viewing tasks, as well as marking them as done or undone
- Remembers user's name and tasks between sessions by saving data to files

## Limitations & Caveats
This program may be inconvenient or impractical for non-programers due to the following points:
- Works only in the command line. There is no GUI (graphical user interface) for this program
- Requires Python to be installed on the user's system
- Displays the list of tasks without pagination. Long lists may be hard to scroll through
- Saves tasks only if the user exits from the menu. Unexpected crashes may result in lost data
