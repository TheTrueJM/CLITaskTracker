from shlex import split as argparse
from TaskTracker import TaskTracker

def runCommand(userInput: str, tracker: TaskTracker) -> bool:
    try:
        command: list[str] = argparse(userInput)
        if len(command) < 1:
            return False
    except ValueError:
        error("Command requires closing quotation")
        return True

    match command[0]:
        case "add":
            add(command, tracker)
        case "update":
            update(command, tracker)
        case "delete":
            delete(command, tracker)
        case "list":
            listTasks(command, tracker)
        case  "mark-in-progress":
            markProgress(command, tracker)
        case  "mark-done":
            markDone(command, tracker)
        case _:
            error("Invalid or unknown command")
    return True


def add(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 2:
        error(f"Command must be specified as 'add [description]'")
        return
    
    taskID = tracker.add(command[1])
    print(f"Task added successfully (ID: {taskID})")

def update(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 3 or not command[1].isdigit():
        error(f"Command must be specified as 'update [taskID] [description]'")
        return
    
    success: bool = tracker.update(int(command[1]), command[2])
    if not success:
        error(f"TaskID {command[1]} does not exist")

def delete(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 2 or not command[1].isdigit():
        error(f"Command must be specified as 'delete [taskID]'")
        return
    
    success: bool = tracker.delete(int(command[1]))
    if not success:
        error(f"TaskID {command[1]} does not exist")


def markProgress(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 2 or not command[1].isdigit():
        error(f"Command must be specified as 'mark-in-porgress [taskID]'")
        return
    
    success: bool = tracker.markStatus(int(command[1]), "in-progress")
    if not success:
        error(f"TaskID {command[1]} does not exist")

def markDone(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 2 or not command[1].isdigit():
        error(f"Command must be specified as 'mark-done [taskID]'")
        return
    
    success: bool = tracker.markStatus(int(command[1]), "done")
    if not success:
        error(f"TaskID {command[1]} does not exist")


def listTasks(command: list[str], tracker: TaskTracker) -> None:
    if len(command) == 1:
        print(tracker.listTasks())
        return
    elif len(command) == 2:
        if command[1] in {"todo", "in-progress", "done"}:
            print(tracker.listTasks(command[1]))
            return
    
    error(f"Command must be specified as 'list' or 'list [todo|in-progress|done]'")


def error(message: str) -> None:
    print(f"!Error: {message}")