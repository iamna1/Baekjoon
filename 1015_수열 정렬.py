n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
for i in range(n):
    for j in range(n):
        if a[i] == b[j]:
            print(j, end = ' ')
            b[j] = None
            break
print()