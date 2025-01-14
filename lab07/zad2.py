
with open('inwokacja.txt', 'r', encoding='utf-8') as file:
    content = file.read()  # Wczytaj całą zawartość pliku
# Oblicz liczbę nowych linii, spacji i tabulacji
newline_count = content.count('\n')  # Liczba nowych linii
space_count = content.count(' ')  # Liczba spacji
tab_count = content.count('\t')  # Liczba tabulacji
print(f"Liczba nowych linii: {newline_count}")
print(f"Liczba spacji: {space_count}")
print(f"Liczba tabulacji: {tab_count}")
