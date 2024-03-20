n = int(input("Cities:"))
def check(n):
    s = set()
    for _ in range(n):
        i = input()
        if i not in s:
            s.add(i)
        else:
            return "REPEAT"
    return "OK"
print(check(n))