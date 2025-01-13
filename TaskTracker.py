from Task import Task

class TaskTracker:
    def __init__(self) -> None:
        self.id_counter: int = 1
        self.tasks: dict[int: Task] = {}
    
    def add(self, description: str) -> int:
        self.tasks[self.id_counter] = Task(description)
        self.id_counter += 1
        return self.id_counter - 1
    

    def idExists(self, id: int) -> bool:
        return id in self.tasks


    def update(self, id: int, description: str) -> bool:
        if self.idExists(id):
            self.tasks[id].update(description)
            return True
    
    def markStatus(self, id: int, status: str) -> bool:
        if self.idExists(id):
            self.tasks[id].markStatus(status)
            return True
    
    def delete(self, id: int) -> bool:
        if self.idExists(id):
            self.tasks.pop(id)
            return True


    def listTasks(self, status: str | None = None) -> str:
        taskList = ""
        for id in self.tasks:
            task = self.tasks[id]
            if status == None or task.status == status:
                taskList += f"Task {id}: {task.listTask()}\n\n"
        return taskList.rstrip() if taskList else f"No tasks avialable"