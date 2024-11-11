def power_of_two(p):
    # Przesunięcie bitowe w lewo o p pozycji, co odpowiada 2^p
    return 1 << p
def main():
    try:
        p = int(input("Podaj wykładnik potęgi (p): "))
        result = power_of_two(p)
        print(f"2^{p} = {result}")
    except ValueError:
        print("Podano nieprawidłową wartość. Proszę podać liczbę całkowitą.")
if __name__ == "__main__":
    main()
