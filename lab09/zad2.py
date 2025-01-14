def medianize(A):
    if not A:  # Sprawdzenie, czy lista nie jest pusta
        return []
    # Obliczenie średniej wartości tablicy
    average = sum(A) / len(A)
    # Odjęcie średniej od każdego elementu tablicy
    result = [x - average for x in A]
    return result
# Przykład użycia
A = [1, 2, 3, 4, 5]
print(medianize(A))