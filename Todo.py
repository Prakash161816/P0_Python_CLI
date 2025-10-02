# Todo.py

class Todo:
    """
    A Todo represents one task with:
    - id (a number),
    - priority (1=high, 3=low),
    - name (what the task is),
    - done (True/False),
    - done_at (when it was finished, or None).
    """

    def __init__(self, id: int, priority: int, name: str, done: bool = False, done_at: str = None):
        self.id = int(id)
        self.priority = int(priority)
        self.name = str(name)
        self.done = bool(done)
        self.done_at = done_at

    def to_dict(self) -> dict:
        """Turn this Todo into a dictionary so we can save it as JSON."""
        return {
            "id": self.id,
            "priority": self.priority,
            "name": self.name,
            "done": self.done,
            "done_at": self.done_at
        }

    def __str__(self) -> str:
        """How the Todo looks when printed."""
        if self.done:
            status="done"
            if self.done_at:
                when=f"(finished{self.done_at})"
            else:
                when=""
        else:
            status="open"
            when=""
        
        return f"id:{self.id}, priority:{self.priority}, task:{self.name}, {status}{when}"

