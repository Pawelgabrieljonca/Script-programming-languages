import random
def get_computer_choice():
    return random.choice(["papier", "kamień", "nożyce"])    # Losowanie wyboru komputera
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:    # Sprawdzenie wyników gry
        return "remis"
    elif (user_choice == "papier" and computer_choice == "kamień") or \
            (user_choice == "kamień" and computer_choice == "nożyce") or \
            (user_choice == "nożyce" and computer_choice == "papier"):
        return "wygrana"
    else:
        return "przegrana"
def rock_paper_scissors_game():
    games_played = 0
    wins = 0
    print("Witaj w grze 'Papier, Kamień, Nożyce'!")
    print("Wybierz 'papier', 'kamień' lub 'nożyce'. Wpisz 'X', aby zakończyć grę.")
    while True:
        user_choice = input("Wybierz papier/kamień/nożyce lub X, aby zakończyć: ").lower()
        if user_choice == "x":
            print("Koniec gry.")
            break
        elif user_choice not in ["papier", "kamień", "nożyce"]:
            print("Nieprawidłowy wybór. Wybierz 'papier', 'kamień', 'nożyce' lub 'X'.")
            continue
        # Losowanie wyboru komputera
        comp_choice = get_computer_choice()
        print(f"Komputer wybrał: {comp_choice}")
        # Określenie wyniku gry
        result = determine_winner(user_choice, comp_choice)
        games_played += 1  # Zliczanie liczby gier
        if result == "wygrana":
            print("Gratulacje, wygrałeś!")
            wins += 1  # Zliczanie wygranych użytkownika
        elif result == "przegrana":
            print("Niestety, przegrałeś.")
        else:
            print("Remis.")
    print(f"Liczba gier: {games_played}, Liczba wygranych: {wins}")
if __name__ == "__main__":
    rock_paper_scissors_game()
