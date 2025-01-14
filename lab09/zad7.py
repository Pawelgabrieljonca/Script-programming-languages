import numpy as np
# Tworzenie przykładowej tablicy 5x5
tablica = np.random.randint(1, 10, (5, 5))  # Tablica z losowymi wartościami od 1 do 9
# Definiowanie wag
wagi = np.array([1, 2, 3, 2, 1])
# Obliczanie średniej ważonej dla każdego wiersza
srednie_wazone = np.dot(tablica, wagi) / sum(wagi)
# Wyświetlenie wyników
print("Tablica:")
print(tablica)
print("\nŚrednie ważone dla każdego wiersza:")
print(srednie_wazone)
