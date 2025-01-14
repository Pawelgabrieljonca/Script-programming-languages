with open('inwokacja.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
# Usuń białe znaki z lewej i prawej strony
lines = [line.strip() for line in lines]

# Liczba wierszy
line_count = len(lines)

# Inicjalizuj zmienne do sumowania znaków i wyrazów
total_bag = 0
total_words = 0

for i, line in enumerate(lines, start=1):# Przetwarzaj każdy wiersz
    char_count = len(line)  # Liczba znaków w wierszu
    word_now = len(line.split())  # Liczba wyrazów w wierszu
    total_bag += char_count
    total_words += word_now
    print(f"Wiersz {i}: {char_count} znaków, {word_now} wyrazów")

print(f"\nLiczba wierszy: {line_count}")
print(f"Łączna liczba znaków: {total_bag}")
print(f"Łączna liczba wyrazów: {total_words}")
