import re
# Wyrażenie regularne do walidacji daty w formacie DD-MM-YYYY
date_regex = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$"
months = {
    "01": "styczeń",
    "02": "luty",
    "03": "marzec",
    "04": "kwiecień",
    "05": "maj",
    "06": "czerwiec",
    "07": "lipiec",
    "08": "sierpień",
    "09": "wrzesień",
    "10": "październik",
    "11": "listopad",
    "12": "grudzień"
}
# Pobranie daty od użytkownika
user_date = input("Podaj datę w formacie DD-MM-YYYY: ")
# Walidacja daty
match = re.match(date_regex, user_date)
if match:
    day, month, year = match.groups()
    print(f"Podana data jest poprawna. Miesiąc to: {months[month]}")
else:
    print("Podana data jest niepoprawna.")
