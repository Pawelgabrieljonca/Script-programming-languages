import numpy as np

# Przygotowanie przykładowej tablicy
array = np.arange(12)  # Tablica z liczbami od 0 do 11

# Test 1: -1 jako pierwszy parametr
reshaped1 = array.reshape(-1, 3)
print("Test 1: -1 jako pierwszy parametr")
print(reshaped1)

# Test 2: -1 jako drugi parametr
reshaped2 = array.reshape(4, -1)
print("\nTest 2: -1 jako drugi parametr")
print(reshaped2)
