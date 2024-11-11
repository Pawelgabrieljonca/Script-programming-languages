import math
import sys
def test_math_functions():
    """Testuje metody math.trunc, math.floor, math.ceil dla przykładowej liczby zmiennoprzecinkowej."""
    a = 5.7  # Przykładowa liczba do testów
    print(f"math.trunc({a}) = {math.trunc(a)}")  # Zaokrąglenie do 0
    print(f"math.floor({a}) = {math.floor(a)}")  # Zaokrąglenie w dół
    print(f"math.ceil({a}) = {math.ceil(a)}")    # Zaokrąglenie w górę

def test_python_version_for_lcm_gcd():
    """Sprawdza wersję Pythona i testuje metody math.lcm oraz math.gcd dla przykładowych liczb, jeśli wersja >= 3.9."""
    if sys.version_info >= (3, 9):
        print("\nWersja Pythona 3.9 lub wyższa wykryta.")
        a, b = 15, 20  # Przykładowe liczby do testów
        print(f"math.lcm({a}, {b}) = {math.lcm(a, b)}")  # Najmniejsza wspólna wielokrotność
        print(f"math.gcd({a}, {b}) = {math.gcd(a, b)}")  # Największy wspólny dzielnik
    else:
        print("\nWersja Pythona jest poniżej 3.9, funkcje math.lcm() i math.gcd() nie będą testowane.")

def test_check_abs_function():
    """Sprawdza, czy moduł math zawiera funkcję do obliczania wartości bezwzględnej."""
    if hasattr(math, "fabs"):
        print(f"math.fabs(-10.5) = {math.fabs(-10.5)}")  # Wartość bezwzględna liczby zmiennoprzecinkowej
    else:
        print("Moduł math nie zawiera funkcji do obliczania wartości bezwzględnej.")

def main():
    test_math_functions()  # Testowanie funkcji trunc, floor i ceil
    test_python_version_for_lcm_gcd()  # Testowanie wersji Pythona i funkcji lcm oraz gcd
    test_check_abs_function() # Sprawdzenie funkcji wartości bezwzględnej
if __name__ == "__main__":
    main()
