import re
# Przykładowy adres
adres = "Al. prof. S. Kaliskiego 7 85-796 Bydgoszcz"
# Wyrażenie regularne takie proste
regex = r"(?:Al\.|ul\.|pl\.)\s*(?:[a-z]+\.\s*)?(?:[A-Z]\.\s*)?([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ ]+)"
# Dopasowanie
match = re.match(regex, adres)
if match:
    street_name = match.group(1)
    print(f"Nazwa ulicy: {street_name}")
else:
    print("Nie udało się dopasować nazwy ulicy.")
