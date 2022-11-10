import sys
sys.setrecursionlimit(10 ** 8)

while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    c = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]

    def dfs(i, j):
        visited[i][j] = 1
        for u in (-1, 0, 1):
            for v in (-1, 0, 1):
                if u == 0 and v == 0:
                    continue
                p, q = i + u, j + v
                if 0 <= p < h and 0 <= q < w:
                    if visited[p][q] == 1 or c[p][q] == 0:
                        continue
                    dfs(p, q)

    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                ans += 1
    print(ans)