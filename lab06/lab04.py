from io import UnsupportedOperation

try:
    # Próba odczytu całego pliku
    with open(r'C:\pawel\Dokumenty\03 - studia\Skryptowe Języki programowania\lab06\plik.txt', "r") as f:
        print(f.read())
except FileNotFoundError:
    print("The file does not exist! Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


try:
    # Próba odczytu jednej linii
    with open("plik.txt", "r") as f:
        print(f.readline())
except FileNotFoundError:
    print("The file does not exist! Please check the file path.")


try:
    # Próba odczytu pierwszych 10 znaków
    with open("plik.txt", "r") as f:
        print(f.read(10))
except FileNotFoundError:
    print("The file does not exist! Please check the file path.")

try:
    # Odczyt w pętli
    with open("thefile.txt", "r") as f:
        for x in f:
            print(x)
except FileNotFoundError:
    print("The file does not exist! Please check the file path.")

try:
    # Odczyt wszystkich linii do listy
    with open("plik.txt", "r") as f:
        lines = f.readlines()  # Wszystkie linie do listy
        print(lines)
except FileNotFoundError:
    print("The file does not exist! Please check the file path.")

try:
    # Próba zapisu do pliku otwartego w trybie odczytu
    with open("plik.txt", "r") as f:
        f.write("Attempt to write")  # Nie można zapisać do pliku otwartego w trybie odczytu
except UnsupportedOperation:
    print("Cannot write to a file opened in read mode!")
except FileNotFoundError:
    print("The file does not exist! Please check the file path.")
