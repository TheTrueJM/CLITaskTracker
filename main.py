from shlex import split as argparse
from TaskTracker import *



def main():
    tracker: TaskTracker = TaskTracker()
    userInput: str = input()
    while completeCommand(userInput, tracker):
        userInput = input()



def completeCommand(userInput: str, tracker: TaskTracker) -> bool:
    command: list[str] = argparse(userInput)
    if len(command) < 1:
        return False
    
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
            error(command)
    return True


def add(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 2:
        return
    
    taskID = tracker.add(command[1])
    print(f"Task added successfully (ID: {taskID})")

def update(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 3:
        return
    if not command[1].isdigit():
        return
    
    tracker.update(int(command[1]), command[2])

def delete(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 2:
        return
    if not command[1].isdigit():
        return
    
    tracker.delete(int(command[1]))


def markProgress(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 2:
        return
    if not command[1].isdigit():
        return
    
    tracker.markStatus(int(command[1]), "in-progress")

def markDone(command: list[str], tracker: TaskTracker) -> None:
    if len(command) != 2:
        return
    if not command[1].isdigit():
        return
    
    tracker.markStatus(int(command[1]), "done")


def listTasks(command: list[str], tracker: TaskTracker) -> None:
    if len(command) == 1:
        print(tracker.listTasks())
    elif len(command) == 2:
        if command[1] in {"todo", "in-progress", "done"}:
            print(tracker.listTasks(command[1]))
        else:
            pass
    else:
        return

def error(command: list[str]) -> None:
    pass



if __name__ == "__main__":
    main()