from collections import deque

h, w, n = map(int, input().split())
f = [input() for _ in range(h)]
ans = 0
l = [[0, 0]] * (n + 1)
for i in range(h):
    for j in range(w):
        p = f[i][j]
        if p == "S":
            l[0] = [i, j]
        elif p == "." or p == "X":
            continue
        else:
            l[int(p)] = [i, j]

for i in range(n):
    dist = [[-1] * w for _ in range(h)]
    si, sj = l[i]
    gi, gj = l[i + 1]
    dist[si][sj] = 0
    q = deque()
    q.append((si, sj))
    while q:
        y, x = q.popleft()
        for u, v in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= y + u < h and 0 <= x + v < w:
                if f[y + u][x + v] == "X":
                    continue
                if dist[y + u][x + v] > -1:
                    continue
                dist[y + u][x + v] = dist[y][x] + 1
                q.append((y + u, x + v))
    ans += dist[gi][gj]
print(ans)