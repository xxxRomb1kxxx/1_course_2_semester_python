import numpy as np

data = np.random.randn(10, 4)

min_value = np.min(data)
max_value = np.max(data)
mean_value = np.mean(data)
std_deviation = np.std(data)


first_five_rows = data[:5, :]

print(min_value,max_value,mean_value,std_deviation,first_five_rows)
