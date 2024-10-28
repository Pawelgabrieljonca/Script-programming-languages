def function_creating_list():
    numbers = []

    # Wypełnianie listy 10 liczbami
    while len(numbers) < 10:
        try:
            num = float(input("Podaj liczbę (pozostało {} do wprowadzenia): ".format(10 - len(numbers))))
            numbers.append(num)
        except ValueError:
            print("Proszę podać poprawną liczbę.")

    numbers.sort()#Sortowanie listy

    # Największy i najmniejszy element
    min_number = numbers[0]
    max_number = numbers[-1]

    # Obliczanie średniej liczb nieujemnych
    non_negative_numbers = [num for num in numbers if num >= 0]
    averagey_non_negative = sum(non_negative_numbers) / len(non_negative_numbers) if non_negative_numbers else 0

    print("Liczby:", numbers)
    print("Najmniejsza liczba:", min_number)
    print("Największa liczba:", max_number)
    print("Średnia liczb nieujemnych:", average_non_negative)

# Wywołanie funkcji
def main():
    function_creating_list()

if __name__ == '__main__':
    main()
