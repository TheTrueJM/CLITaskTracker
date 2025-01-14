from datetime import datetime

# An object which contains the details of a task
class Task:
    def __init__(self, description: str, status: str = "todo") -> None:
        self.description = description
        self.status = status
        self.createdAt = self.updatedAt = datetime.now()
    
    # Update the description of the task
    def update(self, description: str) -> None:
        self.description = description
        self.updatedAt = datetime.now()

    # Mark the status of the task
    def markStatus(self, status: str) -> None:
        self.status = status
        self.updatedAt = datetime.now()
    
    # List all details of the task 
    def listTask(self) -> str:
        return f"""{self.description}
Status: {self.status}
Created At: {self.createdAt:%d/%m/%y %I:%M:%S%p}
Updated At: {self.updatedAt:%d/%m/%y %I:%M:%S%p}"""