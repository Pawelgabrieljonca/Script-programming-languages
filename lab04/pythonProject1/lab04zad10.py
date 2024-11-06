class Student:
    def __init__(self, name: str, last_name: str, index: int):
        self.name = name
        self.last_name = last_name
        self.index = index

    def __eq__(self, other) -> bool:
        if not isinstance(other, Student):
            return False
        return self.index == other.index
