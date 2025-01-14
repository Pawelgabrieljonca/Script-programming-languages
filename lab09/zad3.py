import numpy as np

def medianize(A):
    if not A:  # Sprawdzenie, czy lista nie jest pusta
        return []
    # Obliczenie średniej wartości tablicy
    average = sum(A) / len(A)
    # Odjęcie średniej od każdego elementu tablicy
    result = [x - average for x in A]
    return result

def matrix():
    # Generowanie macierzy 5x5 z liczbami naturalnymi mniejszymi od 100
    matrix = np.random.randint(0, 100, (5, 5))
    print("Macierz:")
    print(matrix)
    # Największy element globalnie
    max_global = np.max(matrix)
    print("Największy element globalnie:", max_global)
    # Największy element w każdym wierszu
    max_rows = np.max(matrix, axis=1)
    print("Największy element w każdym wierszu:", max_rows)
    # Największy element w każdej kolumnie
    max_cols = np.max(matrix, axis=0)
    print("Największy element w każdej kolumnie:", max_cols)
# Przykład użycia
A = [1, 2, 3, 4, 5]
print(medianize(A))
matrix()
