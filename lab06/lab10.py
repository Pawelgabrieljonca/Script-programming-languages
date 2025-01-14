import struct
def save_num(text_file, binary_file, numbers):
    try:
        # Zapis liczb w pliku tekstowym
        with open(text_file, 'w') as txt_file:
            for number in numbers:
                txt_file.write(f"{number}\n")  # Każda liczba w nowej linii
        print(f"Numbers successfully written to {text_file}.")  # Informacja o sukcesie

        # Zapis liczb w pliku binarnym
        with open(binary_file, 'wb') as bin_file:
            for number in numbers:
                bin_file.write(struct.pack('i', number))  # Zapis liczby jako 4-bajtowego int
        print(f"Numbers successfully written in binary format to {binary_file}.")  # Informacja o sukcesie

    except Exception as e:
        print(f"An error occurred: {e}")  # Obsługa błędów

# Przykład użycia funkcji
if __name__ == "__main__":
    numbers = [12, 34, 56, 78, 90]  # Lista liczb
    save_num("numbers.txt", "numbers.bin", numbers)  # Wywołanie funkcji
