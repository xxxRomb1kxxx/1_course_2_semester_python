matrix = [
    [10, 12, 20],
    [20, 13, 40],
    [30, 14, 60]
]
a = [matrix[0][0],matrix[1][0],matrix[2][0]]
b = [matrix[0][1],matrix[1][1],matrix[2][1]]
c = [matrix[0][2],matrix[1][2],matrix[2][2]]
def check(x,y):
    alpha = y[0] / x[0]
    expressible = True
    for i in range(len(y)):
        if y[i] != alpha * x[i]:
            expressible = False
            break 
    return expressible
if check(a,c):
    print("yes")
else:
    print("no")