class Student:
    def __init__(self, name: str, last_name: str, index: int):
        self.name = name
        self.last_name = last_name
        self.index = index
        print("Inicjalizator klasy Student został wywołany")

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name}"

class GraduateStudent(Student):
    def __init__(self, name: str, last_name: str, index: int, thesis_title: str):
        # Wywołanie inicjalizatora klasy nadrzędnej (Student)
        super().__init__(name, last_name, index)
        self.thesis_title = thesis_title
        print("Inicjalizator klasy GraduateStudent został wywołany")

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name}, Thesis: {self.thesis_title}"

# Tworzenie instancji GraduateStudent
grad_student = GraduateStudent("Paweł", "Jońca", 123456, "Second year student")

# Sprawdzenie słownika atrybutów
print(grad_student.__dict__)
