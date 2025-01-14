import re
# Wyrażenie regularne dla adresów e-mail Gmail
gmail_regex = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
# Funkcja walidacji
def validate_gmail(email):
    return bool(re.match(gmail_regex, email))
emails = ["example@gmail.com", "invalid-email@gmail", "user@othermail.com", "test123@gmail.com"]
for email in emails:
    print(f"{email}: {'Valid' if validate_gmail(email) else 'Invalid'}")
