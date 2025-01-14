# CLI Task Tracker
A solution to the [Task-Tracker](https://roadmap.sh/projects/task-tracker) project available on [roadmap.sh](https://roadmap.sh). <br>
(explaination)
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
# Add new task
add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Update task description
update 1 "Buy groceries and cook dinner"

# Mark task as in progress
mark-in-progress 1

# Mark task as done
mark-done

# Delete task
delete 1

# List all tasks
list

# List tasks by status
list todo
list in-progress
list done
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
