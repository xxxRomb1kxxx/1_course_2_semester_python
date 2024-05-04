import numpy as np
x = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
nonzero_indices = np.nonzero(x)[0]
print(nonzero_indices)
