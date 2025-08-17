import sys

# 파이썬 재귀 호출 깊이 제한을 늘려줍니다.
# DFS는 재귀를 많이 사용하기 때문에 이 코드가 필요합니다.
sys.setrecursionlimit(10**6)
def dfs (matrix, r, c, m, n):
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    matrix[r][c] = 0
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0<=nr<n and 0<=nc<m:
            if matrix[nr][nc] == 1:
                dfs(matrix, nr, nc, m, n)
        
T = int(sys.stdin.readline())

cnt = []
for t in range(T):
    cnt.append(0)
    m, n, k = map(int, sys.stdin.readline().split())
    matrix = [[0 for _ in range(m)]for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dfs(matrix, i, j, m, n)
                cnt[t] += 1
for result in cnt:
    print(result)
                       
                        