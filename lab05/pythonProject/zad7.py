import math
def check_trig_identity():
    for angle_degrees in range(91):  # Zakres od 0 do 90 stopni
        # Konwersja kąta na radiany
        angle_radians = math.radians(angle_degrees)
        sin_square = math.sin(angle_radians) ** 2# Obliczenie sin^2(theta) + cos^2(theta)
        cos_square = math.cos(angle_radians) ** 2
        result = sin_square + cos_square
        if round(result, 6) == 1.0:# Sprawdzenie, czy wynik jest równy 1 z dokładnością do 6 miejsc po przecinku
            print(f"Kąt: {angle_degrees}°, Wynik: {result:.6f} - Zgadza się")
        else:
            print(f"Kąt: {angle_degrees}°, Wynik: {result:.6f} - Nie zgadza się")
if __name__ == "__main__":
    check_trig_identity()
