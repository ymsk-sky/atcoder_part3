from collections import deque

n, m = map(int, input().split())
s = [input() for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if s[i][j] == ".":
            continue
        vis = [[0] * m for _ in range(n)]
        for p in range(n):
            for q in range(m):
                if s[p][q] == "#":
                    vis[p][q] = 1
        que = deque([(i, j)])
        while que:
            ci, cj = que.popleft()
            for u, v in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = ci + u, cj + v
                if 0 > ni or ni >= n or 0 > nj or nj >= m:
                    continue
                if vis[ni][nj]:
                    continue
                vis[ni][nj] = 1
                que.append((ni, nj))
        if all([all(e) for e in vis]):
            ans += 1
print(ans)
