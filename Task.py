from datetime import datetime

class Task:
    def __init__(self, description: str, status: str = "todo") -> None:
        self.description = description
        self.status = status
        self.createdAt = self.updatedAt = datetime.now()
    
    def update(self, description: str) -> None:
        self.description = description
        self.updatedAt = datetime.now()

    def markStatus(self, status: str) -> None:
        self.status = status
        self.updatedAt = datetime.now()
    
    def listTask(self) -> str:
        return f"""{self.description}
Status: {self.status}
Created At: {self.createdAt:%d/%m/%y %I:%M:%S%p}
Updated At: {self.updatedAt:%d/%m/%y %I:%M:%S%p}"""