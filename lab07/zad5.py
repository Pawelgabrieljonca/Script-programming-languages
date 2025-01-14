import re  # Import modułu do wyrażeń regularnych
# Otwórz plik i wczytaj jego zawartość
with open('numery.txt', 'r', encoding='utf-8') as file:
    phone_numbers = file.readlines()  # Wczytaj wszystkie linie jako listę
# Usuń białe znaki i znajdź polskie numery telefonów
polish_numbers = [num.strip() for num in phone_numbers if re.match(r'^(?:\+48|0048)', num.strip())]
# Wypisz polskie numery telefonów
print("Polskie numery telefonów:")
for number in polish_numbers:
    print(number)
