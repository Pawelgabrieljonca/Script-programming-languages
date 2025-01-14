import numpy as np
# np.set_printoptions(precision=3)  # 3 miejsca po przecinku
# print(np.array([1.123456, 2.345678]))
#
# np.set_printoptions(suppress=True)
# print(np.array([1.23e-10, 1.23e+10]))
# np.set_printoptions(threshold=5)  # Pokaż maksymalnie 5 elementów
# print(np.arange(10))

# np.set_printoptions(linewidth=50)
# print(np.arange(20).reshape(4, 5))
# # Tablica będzie łamana w liniach o szerokości do 50 znaków


np.set_printoptions(formatter={'float': '{:0.1f}'.format})
print(np.array([1.2345, 2.3456]))

