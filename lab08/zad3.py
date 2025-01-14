import re
# Wczytuje plik
file_path = "adresy.txt"
with open(file_path, "r", encoding="utf-8") as file:
    data = file.readlines()
# Definicja wyrażenia regularnego o taka nie długa
regex = r"ul\. ([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ ]+) (\d+)(?:/(\d+))? (\d{2}-\d{3}) ([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ ]+)"
# Przetwarzanie adresow z uzyciem peli
for line in data:
    match = re.match(regex, line.strip())
    if match:
        ulica = match.group(1)
        numer_domu = match.group(2)
        numer_mieszkania = match.group(3) if match.group(3) else "brak"
        kod_pocztowy = match.group(4)
        miasto = match.group(5)
        print(f"Ulica: {ulica}")
        print(f"Numer domu: {numer_domu}")
        print(f"Numer mieszkania: {numer_mieszkania}")
        print(f"Kod pocztowy: {kod_pocztowy}")
        print(f"Miasto: {miasto}")
        print()
    else:
        print(f"Nie udało się dopasować adresu w linii: {line.strip()}")
