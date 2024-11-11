def get_bit(num, index):
    # Sprawdzenie, czy liczba jest w zakresie 0-255
    if not (0 <= num <= 255):
        raise ValueError("Liczba musi być w zakresie 0-255.")
    # Sprawdzenie, czy indeks bitu jest nieujemny i mieści się w zakresie 0-7
    if not (0 <= index <= 7):
        raise ValueError("Indeks bitu musi być w zakresie 0-7.")

    # Przesunięcie bitowe
    return (num >> index) & 1

def main():
    try:#pobranie liczby oraz indeksu od użytkownika
        num = int(input("Podaj liczbę (0-255): "))
        index = int(input("Podaj indeks bitu (0-7): "))
        result = get_bit(num, index)
        print(f"Wartość bitu na pozycji {index} w liczbie {num} wynosi: {result}")
    except ValueError as e:
        print("Błąd:", e)
if __name__ == "__main__":
    main()
