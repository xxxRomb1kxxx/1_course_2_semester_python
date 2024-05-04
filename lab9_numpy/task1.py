import numpy as np

matrix = np.loadtxt('task1.txt', delimiter=',')

total_sum = np.sum(matrix)
max_element = np.max(matrix)
min_element = np.min(matrix)

print(total_sum)
print(max_element)
print(min_element)