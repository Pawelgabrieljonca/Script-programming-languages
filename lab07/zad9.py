import os
import re
# Wyrażenie regularne do walidacji rozszerzenia pliku .txt
file_regex = r"^.+\.txt$"
# Pobranie ścieżki katalogu od użytkownika
directory = input("Podaj ścieżkę katalogu: ")
# Sprawdzenie, czy katalog istnieje
if os.path.isdir(directory):
    print("Pliki z rozszerzeniem .txt w katalogu:")
    for file_name in os.listdir(directory):
        if re.match(file_regex, file_name):
            print(file_name)
else:
    print("Podany katalog nie istnieje.")
