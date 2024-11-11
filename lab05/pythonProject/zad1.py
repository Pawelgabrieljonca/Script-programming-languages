def get_base():
    while True:# Funkcja pobiera podstawę systemu liczbowego od użytkownika i sprawdza poprawność
        try:
            base = int(input("Enter the base of the number system (2, 8, 10, or 16): "))
            if base in [2, 8, 10, 16]:
                return base
            else:
                print("Invalid base. Choose 2, 8, 10, or 16.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_number(base):
    while True:# Funkcja pobiera liczbę od użytkownika w wybranej podstawie i konwertuje ją do systemu dziesiętnego
        number = input(f"Enter a number in base {base}: ")
        try:# Konwersja liczby do systemu dziesiętnego przy użyciu podanej podstawy
            decimal_val = int(number, base)
            return decimal_val
        except ValueError:
            print(f"Invalid number for base {base}. Please try again.")
def main():
    base = get_base()
    decimal_number = get_number(base)
    print("Number in binary system:", bin(decimal_number))
    print("Number in octal system:", oct(decimal_number))
    print("Number in decimal system:", decimal_number)
    print("Number in hexadecimal system:", hex(decimal_number))

if __name__ == "__main__":
    main()# Wywołanie głównej funkcji
