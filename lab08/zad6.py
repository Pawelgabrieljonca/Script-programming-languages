import re
def check_pasw(password):
    # Słabe hasło: co najmniej 6 znaków
    weak = r"^.{6,}$"
    # Średnie hasło: co najmniej 8 znaków, litera i cyfra
    medium = r"^(?=.*[A-Za-z])(?=.*\d).{8,}$"
    # Mocne hasło: co najmniej 10 znaków, małe i wielkie litery, cyfra, znak specjalny
    strong = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{10,}$"
    if re.match(strong, password):
        return "Mocne"
    elif re.match(medium, password):
        return "Średnie"
    elif re.match(weak, password   ):
        return "Słabe"
    else:
        return "Nie spełnia minimalnych wymagań"
# Przykładowe testy
paswords = [
    "12345",       # Zbyt krótkie
    "abcdef",      # Słabe
    "abc12345",    # Średnie
    "Abc12345!",   # Mocne
    "Pass1@",      # Średnie
    "Abcdef@123",  # Mocne
]
for password in paswords:
    print(f"Hasło: {password} -> Siła: {check_pasw(password)}")
