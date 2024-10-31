class Student:
    quantity = 0  # Atrybut klasowy

    def __init__(self, name="", last_name=""):
        self.name = name
        self.last_name = last_name
        self.marks = []
        Student.quantity += 1

    def __check_name_fields(self) -> bool:
        """Funkcja wewnętrzna sprawdzająca, czy pola name i last_name nie są puste"""
        return bool(self.name) and bool(self.last_name)

    def say_hello(self):
        """Funkcja wypisująca powitanie, jeśli pola name i last_name są wypełnione"""
        if self.__check_name_fields():
            print(f"Hello, {self.name} {self.last_name}!")
        else:
            print("Imię i/lub nazwisko są puste.")

# Tworzenie obiektów Student i sprawdzanie działania funkcji
s1 = Student("Paweł", "Jońca")
s1.say_hello()  # Powinno wypisać "Hello, Paweł Kowalski!"

s2 = Student("", "Jońca")
s2.say_hello()  # Powinno wypisać "Imię i/lub nazwisko są puste."

# Próba wywołania funkcji __check_name_fields spoza klasy
try:
    print(s1.__check_name_fields())
except AttributeError as e:
    print(f"Błąd: {e}")
