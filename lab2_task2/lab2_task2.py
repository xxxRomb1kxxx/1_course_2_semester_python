from math import factorial
rows = int(input(""))
for i in range(rows):
    for j in range(rows-i+1):
        print(end=" ")
    for j in range(i+1):
        nCr = factorial(i) // (factorial(j) * factorial(i-j))
        if nCr % 2 == 0:
            print(" ",end = " ")
        else:
            print("*",end = " ")
        if j == i+1:
            print("*",end = " ")
    print()
for i in range(rows+2):
    print("*", end=" ")
  
