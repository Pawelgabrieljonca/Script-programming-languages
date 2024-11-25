x = -1

try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
    if x < 0:
        raise ValueError("Sorry, no numbers below zero")
except Exception as e:
    print(f"error {e}") #wyświetla szczegóły przechyconego wyjątku
