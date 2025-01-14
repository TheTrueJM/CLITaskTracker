from Task import Task

# An object which keeps track of a range of tasks identified by unique ID numbers
class TaskTracker:
    def __init__(self) -> None:
        self.id_counter: int = 1
        self.tasks: dict[int: Task] = {}
    
    # Create a new task and add it to the tracker
    def add(self, description: str) -> int:
        self.tasks[self.id_counter] = Task(description)
        self.id_counter += 1
        return self.id_counter - 1
    

    # Check that an ID exists in the tracker
    def idExists(self, id: int) -> bool:
        return id in self.tasks


    # Update the description of the task with tracker ID
    def update(self, id: int, description: str) -> bool:
        if self.idExists(id):
            self.tasks[id].update(description)
            return True
    
    # Mark the status of the task with tracker ID
    def markStatus(self, id: int, status: str) -> bool:
        if self.idExists(id):
            self.tasks[id].markStatus(status)
            return True
    
    # Delete a task from the tracker
    def delete(self, id: int) -> bool:
        if self.idExists(id):
            self.tasks.pop(id)
            return True


    # List all tracked tasks or only the tasks matching a specific status
    def listTasks(self, status: str | None = None) -> str:
        taskList = ""
        for id in self.tasks:
            task = self.tasks[id]
            if status == None or task.status == status:
                taskList += f"Task {id}: {task.listTask()}\n\n"
        return taskList.rstrip() if taskList else f"No tasks avialable"