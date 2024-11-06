from typing import List #importuje List z modułu typing aby określić typ listy przechowujący oceny marks
class Student: #tworzę klasę Student
    def __init__(self): #konstruktor __init__
        self.name = ""
        self.last_name = ""
        self.marks = []
        self.index_number = None
    def give_name(self, name: str, last_name: str) -> None: #Metoda ustawia imię i nazwisko studenta i przyjmuje dwa argumenty name i last_name, zapisuje je w obiekcie
        self.name = name
        self.last_name = last_name
    def give_mark(self,mark: int) -> None: #metoda pozwala dodac ocenę do listy ocen (marks)
        #Argument mark jest dodawany do listy
        self.marks.append(mark)
    def get_marks(self) -> List[int]: return self.marks #zwraca listę wszystkich ocen
    def calculate_average(self) -> float:#Metoda oblicza średnią ocen, jeśli lista jest pusta zwraca 0.0
        if not self.marks:
            return 0.0
        return sum(self.marks)/len(self.marks)
    def assign_index_number(self, index_number: int) -> None: #metoda przypisuje numer indeksu
        self.index_number = index_number
    def say_hello(self) -> None:
        print(f"Hello! I'm {self.name} {self.last_name}, my index number is {self.index_number}")

s = Student()             # Tworzymy obiekt studenta
s.give_name("Paul", "Jonnes") # Ustawiamy imię i nazwisko na "Jane Doe"
s.assign_index_number(123456) # Przypisujemy numer indeksu 123456
s.give_mark(5)            # Dodajemy ocenę 5 do listy ocen
Student.give_mark(s, 3)   # Dodajemy ocenę 3 w alternatywny sposób (bezpośrednio wywołując funkcję na klasie)

print(s.get_marks())      # Wyświetla listę ocen: [5, 3]
print("Average mark:", s.calculate_average()) # Wyświetla średnią ocen: 4.0
s.say_hello()             # Wyświetla powitanie z numerem indeksu
