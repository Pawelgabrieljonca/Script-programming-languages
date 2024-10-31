
"""
class Student:
    def __init__(self, name: str, last_name: str, index: int):
        self.name = name
        self.last_name = last_name
        self.index = index

    def __eq__(self, o: 'Student') -> bool:
        return self.index == o.index

    def __ne__(self, o: 'Student') -> bool:
        return self.index != o.index

    def __lt__(self, o: 'Student') -> bool:
        return self.index < o.index

    def __gt__(self, o: 'Student') -> bool:
        return self.index > o.index

# Tworzenie instancji Student
s1 = Student('Joe', 'Doe', 111111)
s2 = Student('Jane', 'Key', 222222)

# Wywołanie repr() i str() bez przeciążania
print(repr(s1))  # Wyświetli domyślną reprezentację obiektu, np. <__main__.Student object at 0x7f96bc1a7be0>
print(str(s1))   # Wyświetli to samo, co repr(), jeśli nie ma __str__
"""
class Student:
    def __init__(self, name: str, last_name: str, index: int):
        self.name = name
        self.last_name = last_name
        self.index = index

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.last_name} {self.name}"

    def __eq__(self, o: 'Student') -> bool:
        return self.index == o.index

    def __ne__(self, o: 'Student') -> bool:
        return self.index != o.index

    def __lt__(self, o: 'Student') -> bool:
        return self.index < o.index

    def __gt__(self, o: 'Student') -> bool:
        return self.index > o.index

# Tworzenie instancji Student
s1 = Student('Joe', 'Doe', 111111)
s2 = Student('Jane', 'Key', 222222)

# Wywołanie repr() i str() po przeciążeniu
print(repr(s1))  # Wyświetli "Joe Doe" z __repr__
print(str(s1))   # Wyświetli "Doe Joe" z __str__
