class Student:
    quantity = 0  # Atrybut klasowy, który będzie przechowywać liczność
    #jest wspólny dla wszystkich instacji klasy
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.marks = []
        Student.quantity += 1  # Zwiększenie liczności przy każdej nowej instancji

# Tworzenie kilku instancji klasy Student
s1 = Student()
s2 = Student()
s3 = Student()

# Sprawdzenie liczności przez poszczególne obiekty
print(s1.quantity)  # Powinno wypisać 3
print(s2.quantity)  # Powinno wypisać 3
print(s3.quantity)  # Powinno wypisać 3

# Sprawdzenie liczności przez klasę
print(Student.quantity)  # Powinno wypisać 3
