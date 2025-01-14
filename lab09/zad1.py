import numpy as np

def replace_zeros(A, x):
    A = np.array(A)
    A[A == 0] = x
    return A

# Przykład użycia
mat = np.array([[0, 2, 0], [4, 0, 6], [0, 8, 9]])
x_val = 3
result = replace_zeros(mat, x_val)
print("Macierz po zamianie zer na", x_val, ":")
print(result)
