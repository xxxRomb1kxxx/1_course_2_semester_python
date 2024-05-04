import numpy as np
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zero_indices = np.where(x == 0)[0]
zero_indices = zero_indices[:-1]
max_after_zero = np.max(x[zero_indices + 1])

print(max_after_zero)