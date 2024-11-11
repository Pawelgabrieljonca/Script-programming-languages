import random
import math
def triangle(a, b, c):
    # Sprawdza czy z wylosowanych boków można stworzyć trójkąt
    return a + b > c and a + c > b and b + c > a

def calculate(a, b, c):
    # Oblicza pole trójkąta
    s = (a + b + c) / 2  # Obliczenie połowy obwodu
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def generate_calculate():
    # Losowanie trzech liczb z zakresu <3, 10>
    a = random.randint(3, 10)
    b = random.randint(3, 10)
    c = random.randint(3, 10)
    print(f"Wylosowane boki: {a}, {b}, {c}")

    # Sprawdzenie, czy z wylosowanych boków można zbudować trójkąt
    if triangle(a, b, c):
        area = calculate(a, b, c)
        print(f"Z boków {a}, {b} i {c} można zbudować trójkąt. Pole trójkąta wynosi: {area:.2f}")
    else:
        print("Nie można utworzyć trójkąta z tych boków.")
def main():
    generate_calculate()
if __name__ == "__main__":
    main()