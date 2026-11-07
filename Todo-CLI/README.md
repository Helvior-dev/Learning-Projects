# Todo-CLI

A small interactive command-line task manager that stores tasks in a JSON file.

## Features

- Add one or more tasks.
- List tasks and their completion status.
- Mark a task as completed.
- Delete a task.
- Save task data to `todos.json`.

## Requirements

- Python 3.6 or newer
- No third-party packages

## Usage

Run the script and follow the prompts. The menu and prompts are in Russian.

```bash
python todo-cli.py
```

Menu options:

1. Add tasks.
2. Show all tasks and their status.
3. Mark a task as completed.
4. Delete a task.
0. Exit.

The program reads and writes `todos.json` in the current working directory. If the file does not exist, the task list starts empty. Task actions use the task's 1-based position in the current list, not its displayed ID.
