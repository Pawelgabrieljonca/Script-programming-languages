import math
def ladder_height(ladder_length, angle_degrees):
    angle_radians = math.radians(angle_degrees)    # Konwersja kąta z stopni na radiany
    height = ladder_length * math.sin(angle_radians)# Obliczenie wysokości
    return height
def main():
    print("Test na jaką wysokość sięgnie drabina")
    try:
        ladder_length = float(input("Podaj długość drabiny (w metrach): "))
        angle_degrees = float(input("Podaj kąt między drabiną a poziomem (w stopniach): "))
        if ladder_length <= 0 or angle_degrees <= 0 or angle_degrees >= 90:
            print("Błędne dane. Długość drabiny musi być dodatnia, a kąt musi być z zakresu (0, 90) stopni.")
            return
        height = ladder_height(ladder_length, angle_degrees)
        print(f"Wysokość, na jaką sięga koniec drabiny, wynosi: {height:.2f} metra/ów")
    except ValueError:
        print("Podaj poprawne wartości.")
if __name__ == "__main__":
    main()
