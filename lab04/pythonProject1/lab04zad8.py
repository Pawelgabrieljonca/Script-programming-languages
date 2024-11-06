class Student:
    def __init__(self, name: str, last_name: str, index: int):
        self.name = name
        self.last_name = last_name
        self.index = index

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.last_name} {self.name}"

# Tworzenie instancji Student
s1 = Student("Paweł", "Jońca", 122333)

# Wyświetlenie atrybutów instancji jako słownik
print(s1.__dict__)
