class Task:
    id: str
    complete: bool
    title: str

    def __init__(self, id: str, complete: bool, title: str):
        self.id = id
        self.complete = complete
        self.title = title

    def __str__(self) -> str:
        return f"Task id={self.id} complete={self.complete} title={self.title}"
