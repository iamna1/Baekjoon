n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
        continue
    if b % 4 == 0:
        b = 4
    else:
        b %= 4
    print((a ** b) % 10)