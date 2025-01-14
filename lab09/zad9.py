# # def sum_numbers(*args):
# #     return sum(args)
# # result = sum_numbers(1, 2, 3)  # wynik to 6
#
# # a, *b = [1, 2, 3, 4]
# # # a = 1, b = [2, 3, 4]
#
# repeated = [1] * 3  # wynik to [1, 1, 1]

import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = a @ b
print(result)