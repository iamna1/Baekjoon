n, m = map(int, input().split())
basket = [i for i in range(1,n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    test = basket[i-1:j]
    for k in range(len(test)):
        basket[i+k-1] = test[len(test)-k-1]
print(*basket)