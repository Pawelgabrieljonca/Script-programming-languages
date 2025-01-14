import numpy as np
# Wylosowanie 10 liczb do tablicy Numpy
array = np.random.rand(10)  # Liczby losowe z zakresu [0, 1)
print("Oryginalna tablica:", array)
# Sortowanie rosnąco
sorted_array_ascending = np.sort(array)
print("Tablica posortowana rosnąco:", sorted_array_ascending)
# Sortowanie malejąco
sorted_array_descending = np.sort(array)[::-1]  # Odwrócenie kolejności
print("Tablica posortowana malejąco:", sorted_array_descending)
