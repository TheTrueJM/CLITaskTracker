# CLI Task Tracker
A solution to the [Task-Tracker](https://roadmap.sh/projects/task-tracker) project available on [roadmap.sh](https://roadmap.sh).

This project is a simple command-line interface (CLI) application that allows users to manage and track tasks. Task management features adding, updating, deleting, and listing commands. When exiting the application, the currently tracked tasks will be saved to a JSON output file specified by the user.

## Features
- **Add Task:** Create a new task to be tracked
- **Update Task Description:** Updates the description of a task
- **Mark Task Status:** Mark a task's status as "in-progress" or "done"
- **Delete Task:** Delete a task from the tracker
- **Listing Tasks:** Display a list of all tasks or tasks matching a status
- **JSON File Saving:** The tracked tasked will be saved to a specified JSON file

## Installation
```
git clone https://github.com/TheTrueJM/CLITaskTracker.git
cd CLITaskTracker
py ./main.py
```

## Usage
```
# Specify the name of the JSON output file
Enter name for JSON file: MyTasks

# Add new task
add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Update task description
update 1 "Buy groceries and cook dinner"
# Output: Task 1 description successfully updated

# Mark task as in progress
mark-in-progress 1
# Output: Task 1 successfully marked as 'in-progress'

# Mark task as done
mark-done 1
# Output: Task 1 successfully marked as 'done'

# Delete task
delete 1
# Output: Task 1 successfully deleted

# List all tasks
list

# List tasks by status
list todo
list in-progress
list done

# Exit application and save JSON file

# (Enter Nothing)
```

## Sample JSON Output
```json
{
  "1": {
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2025-01-14T12:30:15.000000",
    "updatedAt": "2025-01-14T12:30:15.000000"
  }
}
```
