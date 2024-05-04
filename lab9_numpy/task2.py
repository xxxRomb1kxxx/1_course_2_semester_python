import numpy as np

def run_len_coding(x):
    numbers = []
    frequencies = []
    number = x[0]
    count_repeat_elemets = 1
    for i in range(1,len(x)):
          if x[i] == number:
            count_repeat_elemets += 1
          else:
            numbers.append(number)
            frequencies.append(count_repeat_elemets)
            number = x[i]
            count_repeat_elemets = 1

    numbers.append(number)
    frequencies.append(count_repeat_elemets)
    return np.array(numbers), np.array(frequencies)

x = np.array([1,1,1,1,1,5,5,5,5,5,9,9,9,9,9])
result = run_len_coding(x)
print(result)