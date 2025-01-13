import json
from datetime import datetime
from TaskTracker import TaskTracker, Task
from Commands import runCommand



def main():
    filename: str = getFilename()

    tracker: TaskTracker = TaskTracker()
    userInput = input()
    while runCommand(userInput, tracker):
        userInput = input()

    JSONWrite(filename, tracker)
    print(f"Current tasks saved to JSON file '{filename}'. Goodbye.")


def getFilename() -> str:
    userInput: str = input("Enter name for JSON file: ")
    while not userInput.isalnum():
        userInput = input("Enter name for JSON file: ")
    return userInput + ".json"


def JSONWrite(filename: str, tracker: TaskTracker) -> None:
    tasks_dict: dict[int: dict] = {}

    for taskID in tracker.tasks:
        task: Task = tracker.tasks[taskID]
        tasks_dict[taskID] = {"description": task.description, "status": task.status, "createdAt": task.createdAt, "updatedAt": task.updatedAt}

    tasks_object = json.dumps(tasks_dict, default=serialize)
    with open(filename, "w") as file:
        file.write(tasks_object)

def serialize(object: object):
    if isinstance(object, datetime):
        return object.isoformat()



if __name__ == "__main__":
    main()