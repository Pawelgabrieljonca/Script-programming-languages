import re  # Import modułu do wyrażeń regularnych
# Wczytaj numery telefonów z pliku
with open('numery.txt', 'r', encoding='utf-8') as file:
    phone_numbers = [line.strip() for line in file.readlines()]  # Usuń białe znaki
# Propozycja wyrażeń regularnych dla różnych formatów
patterns = {
    "Format +48 XXXXXXXXX": r'^\+48\d{9}$',  # +48 bez spacji, 9 cyfr
    "Format 0048 XXXXXXXXX": r'^0048\d{9}$',  # 0048 bez spacji, 9 cyfr
    "Format +48 XXX XXX XXX": r'^\+48 \d{3} \d{3} \d{3}$',  # +48 z trzema blokami cyfr
    "Format 0048 XXX XXX XXX": r'^0048 \d{3} \d{3} \d{3}$',  # 0048 z trzema blokami cyfr
    "Format XXXXXXXXX": r'^\d{9}$',  # 9 cyfr, bez prefiksu
}
# Zliczanie numerów w każdym formacie
format_counts = {key: 0 for key in patterns.keys()}
# Sprawdzenie numerów i przypisanie do formatu
for number in phone_numbers:
    for format_name, pattern in patterns.items():
        if re.match(pattern, number):
            format_counts[format_name] += 1
            break  # Gdy znajdziemy dopasowanie, kończymy iterację
print("Liczba numerów w poszczególnych formatach:")
for format_name, count in format_counts.items():
    print(f"{format_name}: {count}")
