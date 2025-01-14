# Otwórz plik do odczytu
with open('inwokacja.txt', 'r', encoding='utf-8') as file:
    content = file.read()  # Wczytaj zawartość pliku
# Zamień wszystkie kropki na wielokropek, pozostawiając wielokropek bez zmian
modified_content = content.replace('...', '<<<TEMP>>>')  # Tymczasowa zamiana wielokropków
modified_content = modified_content.replace('.', '...')  # Zamień kropki na wielokropki
modified_content = modified_content.replace('<<<TEMP>>>', '...')  # Przywróć oryginalne wielokropki
print(modified_content)
