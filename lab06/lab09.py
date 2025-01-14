import json
class Student:
    def __init__(self, name, age, subjects):  # Inicjalizacja instancji studenta
        self.name = name  # Imię studenta
        self.age = age  # Wiek studenta
        self.subjects = subjects  # Lista przedmiotów
    def export_to_file(self, filename):  # Eksportuje dane instancji do pliku JSON
        try:
            data = {'name': self.name, 'age': self.age, 'subjects': self.subjects}  # Dane instancji
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)  # Zapis danych w formacie JSON
            print(f"Data successfully exported to {filename}.")  # Informacja o sukcesie
        except Exception as e:
            print(f"An error occurred during export: {e}")  # Obsługa błędów eksportu
    def import_from_file(self, filename):  # Importuje dane instancji z pliku JSON
        try:
            with open(filename, 'r') as file:
                data = json.load(file)  # Wczytanie danych z pliku
            self.name = data['name']  # Przywrócenie imienia
            self.age = data['age']  # Przywrócenie wieku
            self.subjects = data['subjects']  # Przywrócenie przedmiotów
            print(f"Data successfully imported from {filename}.")  # Informacja o sukcesie
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")  # Obsługa braku pliku
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}.")  # Obsługa błędów formatu JSON
        except KeyError as e:
            print(f"Missing key in data: {e}")  # Obsługa brakujących kluczy
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Obsługa innych wyjątków
if __name__ == "__main__":
    student = Student("Alice", 20, ["Mathematics", "Physics", "Literature"])  # Tworzenie obiektu studenta
    print("Original student data:", student.__dict__)  # Wyświetlenie danych przed eksportem
    student.export_to_file("student_data.json")  # Eksport danych do pliku
    student.name = "Bob"  # Modyfikacja imienia
    student.age = 22  # Modyfikacja wieku
    student.subjects = ["History"]  # Modyfikacja przedmiotów
    print("Modified student data:", student.__dict__)  # Wyświetlenie zmodyfikowanych danych
    student.import_from_file("student_data.json")  # Import danych z pliku
    print("Restored student data:", student.__dict__)  # Wyświetlenie przywróconych danych
