n = int(input())
lst = [int(input()) for _ in range(n)]
s = set()
for i in lst:
    if not i in s:
        s.add(i)
print("unique elemets",len(s))