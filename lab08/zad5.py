import re
# Tekst i wyrażenie regularne
text = "Ala ma kota a kot ma Ale"
pattern = "[a-z]{3}"  # Trzy małe litery z alfabetu
# Dopasowanie bez flagi
no_flag = re.match(pattern, text)
if no_flag:
    print(f"Dopasowanie bez flagi: {no_flag.group()}")
else:
    print("Brak dopasowania bez flagi.")
# Dopasowanie z flagą re.I (ignorowanie wielkości liter)
with_flag = re.match(pattern, text, flags=re.I)
if with_flag:
    print(f"Dopasowanie z flagą re.I: {with_flag.group()}")
else:
    print("Brak dopasowania z flagą.")
