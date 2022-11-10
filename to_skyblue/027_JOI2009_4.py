import sys
sys.setrecursionlimit(10 ** 8)

m = int(input())
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

ans = 0
dist = [[-1] * m for _ in range(n)]
def dfs(i, j):
    global ans
    for u, v in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= i + u < n and 0 <= j + v < m:
            if l[i + u][j + v] == 0:
                continue
            if dist[i + u][j + v] > 0:
                continue
            dist[i + u][j + v] = dist[i][j] + 1
            dfs(i + u, j + v)
            dist[i + u][j + v] = -1
    ans = max(ans, dist[i][j])

for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            continue
        for _i in range(n):
            for _j in range(m):
                dist[_i][_j] = -1
        dist[i][j] = 1
        dfs(i, j)
print(ans)