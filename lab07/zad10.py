import re
# Lista 10 napisów
words = ["lis", "drzewo", "ananas", "pies", "pan", "orzechy", "lizak", "telefon", "papier", "myszka"]
# Elementy kończące się na x lub y
ends_with_x_or_y = [word for word in words if re.search(r"[xy]$", word)]
# Elementy trzyznakowe zaczynające się od a
three_char_starting_a = [word for word in words if re.search(r"^a.{2}$", word)]
# Elementy rozpoczynające się samogłoską
starts_with_vowel = [word for word in words if re.search(r"^[aeiouAEIOU]", word)]
# Wyniki
print("Elementy kończące się na 'x' lub 'y':", ends_with_x_or_y)
print("Elementy trzyznakowe zaczynające się od 'a':", three_char_starting_a)
print("Elementy rozpoczynające się samogłoską:", starts_with_vowel)
