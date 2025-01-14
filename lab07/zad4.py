import re  # Import modułu do wyrażeń regularnych

# Lista imion
names = ["Paweł", "Adam", "Kacper", "Filip", "Szymon", "Artur", "Marcelina", "Kasia", "Kamila"]

# Korzystając z wyrażeń regularnych, znajdź imiona damskie
female_names = [name for name in names if re.match(r'^[A-Z][a-z]*a$', name)]

# Wypisz imiona damskie
print("Imiona damskie rozpoczynające się wielką literą i kończące się na 'a':")
print(female_names)
