T = int(input())
for _ in range(T):
    r, s = input().split()
    r = int(r)
    for j in range(len(s)):
        print(s[j]*r,end = '')
    print()