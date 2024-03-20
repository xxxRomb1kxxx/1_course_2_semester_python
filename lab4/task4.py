def func(str):
    s = {}
    for i in str:
        if i in s:
            print(s[i])
            s[i] += 1
            continue
        print(0)
        s[i] = 1
s = input().split()
func(s)












n = input()
