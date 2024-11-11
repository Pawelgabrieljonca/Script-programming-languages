import random
def flip_coin():
    # Funkcja losująca wynik rzutu monetą: 0 oznacza orła, 1 oznacza reszkę
    return random.choice(["orzeł", "reszka"])
def coin_toss_game():
    games_played = 0
    wins = 0
    print("Hej, miło jest cię tu widzieć!")
    print("Wybierz 'orzeł' lub 'reszka'. Wpisz 'X', aby zakończyć grę.")
    while True:
        # Pobieranie wyboru użytkownika
        user_choice = input("Wybierz orzeł/reszka lub X, aby zakończyć: ").lower()
        if user_choice == "x":
            print("Koniec gry.")
            break
        elif user_choice not in ["orzeł", "reszka"]:
            print("Nieprawidłowy wybór. Wybierz 'orzeł', 'reszka' lub 'X'.")
            continue
        # Wykonanie rzutu monetą
        result = flip_coin()
        games_played += 1  # Zliczanie liczby gier
        print(f"Wynik rzutu: {result}")
        # Sprawdzanie, czy użytkownik wygrał
        if user_choice == result:
            print("Gratulacje, wygrałeś!")
            wins += 1  # Zliczanie wygranych
        else:
            print("Niestety, przegrałeś.")
    print(f"Liczba gier: {games_played}, Liczba wygranych: {wins}")
# Wywołanie funkcji gry
if __name__ == "__main__":
    coin_toss_game()
