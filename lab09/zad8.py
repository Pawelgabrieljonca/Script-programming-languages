import random
from collections import Counter
# Tworzenie tablicy 10x10 z losowymi liczbami
tablica = [[random.randint(0, 10) for _ in range(10)] for _ in range(10)]
# Zliczanie wystąpień liczb w tablicy
flat_tablica = [element for row in tablica for element in row]  # Spłaszczamy tablicę
liczba_wystapien = Counter(flat_tablica)
# Wypisanie tablicy
print("Tablica 10x10:")
for row in tablica:
    print(row)
# Wypisanie liczności wystąpień elementów
print("\nLiczność wystąpień elementów:")
for liczba, wystapienia in liczba_wystapien.items():
    print(f"Liczba {liczba}: {wystapienia} razy")
