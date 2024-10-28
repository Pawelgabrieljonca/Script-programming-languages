def student_grades():
    # Zagnieżdżony słownik z danymi studentów
    students = {
        12345: {
            "imię": "Paweł",
            "nazwisko": "Kowalski",
            "oceny": [4, 5, 3, 4, 5]
        },
        23456: {
            "imię": "Kacper",
            "nazwisko": "Nowak",
            "oceny": [3, 3, 4, 5, 4]
        },
        34567: {
            "imię": "Artur",
            "nazwisko": "Wiśniewski",
            "oceny": [5, 4, 4, 5, 4]
        }
    }
    # Wypisywanie informacji o każdym studencie
    for index, details in students.items():
        imie = details["imię"]
        nazwisko = details["nazwisko"]
        oceny = details["oceny"]
        srednia_ocen = sum(oceny) / len(oceny)
        print(f"Numer indeksu: {index}, Imię: {imie}, Nazwisko: {nazwisko}, Średnia ocen: {srednia_ocen:.2f}")

def main():
    student_grades()

if __name__ == "__main__":
    main()