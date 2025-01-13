from Task import *

class TaskTracker:
    def __init__(self) -> None:
        self.id_counter: int = 1
        self.tasks: dict[int: Task] = {}
    
    def add(self, description: str) -> int:
        self.tasks[self.id_counter] = Task(description)
        self.id_counter += 1
        return self.id_counter - 1

    def update(self, id: int, description: str) -> None:
        self.tasks[id].update(description)
    
    def markStatus(self, id: int, status: str) -> None:
        self.tasks[id].markStatus(status)
    
    def delete(self, id: int) -> None:
        self.tasks.pop(id)

    def listTasks(self, status: str | None = None) -> str:
        taskList = ""
        for id in self.tasks:
            task = self.tasks[id]
            if status == None or task.status == status:
                taskList += f"Task {id}: {task.listTask()}"
        return taskList