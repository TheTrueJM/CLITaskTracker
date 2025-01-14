import json
from datetime import datetime
from TaskTracker import TaskTracker, Task
from Commands import runCommand



# Runs the mainloop of the CLI and writes the tracked tasks to a specified JSON file
def main():
    filename: str = getFilename()

    tracker: TaskTracker = TaskTracker()
    userInput = input("Enter commands to the task tracker:\n")
    while runCommand(userInput, tracker):
        userInput = input()

    JSONWrite(filename, tracker)
    print(f"Current tasks saved to JSON file '{filename}'. Goodbye.")


# Returns a JSON file name entered by the user
def getFilename() -> str:
    userInput: str = input("Enter name for JSON file: ")
    while not userInput.isalnum():
        userInput = input("Enter name for JSON file: ")
    print("Valid JSON file name entered.")
    return userInput + ".json"


# Writes a task tracker to a JSON file
def JSONWrite(filename: str, tracker: TaskTracker) -> None:
    tasks_dict: dict[int: dict] = {}

    # Convert TaskTracker and Task objects to a python dictionary
    for taskID in tracker.tasks:
        task: Task = tracker.tasks[taskID]
        tasks_dict[taskID] = {"description": task.description, "status": task.status, "createdAt": task.createdAt, "updatedAt": task.updatedAt}

    tasks_object = json.dumps(tasks_dict, default=serialize)
    with open(filename, "w") as file:
        file.write(tasks_object)

# Converts python 'datetime' object to a JSON readable format
def serialize(object: object):
    if isinstance(object, datetime):
        return object.isoformat()



if __name__ == "__main__":
    main()