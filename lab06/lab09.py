import json
class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def export_to_file(self, filename):
        try:
            data = {
                'name': self.name,
                'age': self.age,
                'subjects': self.subjects
            }
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data successfully exported to {filename}.")
        except Exception as e:
            print(f"An error occurred during export: {e}")

    def import_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            self.name = data['name']
            self.age = data['age']
            self.subjects = data['subjects']
            print(f"Data successfully imported from {filename}.")
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}.")
        except KeyError as e:
            print(f"Missing key in data: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Tworzenie instancji studenta
    student = Student("Alice", 20, ["Mathematics", "Physics", "Literature"])
    print("Original student data:", student.__dict__)

    student.export_to_file("student_data.json")

    # Modyfikacja danych i ich przywrócenie
    student.name = "Bob"
    student.age = 22
    student.subjects = ["History"]
    print("Modified student data:", student.__dict__)

    # Import danych z pliku
    student.import_from_file("student_data.json")
    print("Restored student data:", student.__dict__)
