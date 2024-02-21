from math import factorial
rows = int(input())
for i in range(rows):
    for j in range(rows-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
    print()
