class Student:
    quantity = 0

    def __init__(self, name="", last_name="", marks=None):
        self.name = name
        self.last_name = last_name
        self.marks = marks if marks is not None else []
        Student.quantity += 1

    def average(self) -> float:
        #Zwraca średnią ocen
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def __lt__(self, other) -> bool:
        return self.average() < other.average()

    def __gt__(self, other) -> bool:
        return self.average() > other.average()

    def __eq__(self, other) -> bool:
        return self.average() == other.average()

    def __le__(self, other) -> bool:
        return self.average() <= other.average()

    def __ge__(self, other) -> bool:
        return self.average() >= other.average()

    def __ne__(self, other) -> bool:
        return self.average() != other.average()

# Tworzenie obiektów Student z różnymi ocenami
s1 = Student("Paweł", "Jońca", [3, 4, 5])
s2 = Student("Szymon", "Stawarz", [5, 5, 5])
s3 = Student("Jakub", "Smolarek", [3, 3, 3])
# Testowanie operatorów porównania
print(s1 < s2)   # True, bo średnia s1 (4.0) jest mniejsza niż średnia s2 (5.0)
print(s1 > s3)   # True, bo średnia s1 (4.0) jest większa niż średnia s3 (3.0)
print(s1 == s2)  # False, bo średnie są różne
print(s1 <= s3)  # False, bo średnia s1 (4.0) nie jest mniejsza ani równa średniej s3 (3.0)
print(s1 >= s2)  # False, bo średnia s1 (4.0) nie jest większa ani równa średniej s2 (5.0)
print(s1 != s3)  # True, bo średnie są różne
