T = int(input())
result = []
for j in range(T):
    result.append(0)
    point = list(map(int, input().split()))
    n = int(input())
    for i in range(n):
        x, y, r = map(int, input().split())
        if (point[0] - x)**2 + (point[1] - y)**2 < r**2:
            if(point[2] - x)**2 + (point[3] - y)**2 > r**2:
                result[j] += 1
        else:
            if(point[2] - x)**2 + (point[3] - y)**2 < r**2:
                result[j] += 1
for a in result:
    print(a)
