from collections import deque

a, b = map(int, input().split())
a, b = a - 1, b - 1
sl = [input() for _ in range(3)]
ml = []
for i in range(3):
    for j in range(3):
        if sl[i][j] == "#":
            ml.append((i - 1, j - 1))
vis = [[0] * 9 for _ in range(9)]
vis[a][b] = 1
ans = 1
que = deque([(a, b)])
while que:
    i, j = que.popleft()
    for p, q in ml:
        u, v = i + p, j + q
        if 0 > u or u > 8 or 0 > v or v > 8:
            continue
        if vis[u][v]:
            continue
        vis[u][v] = 1
        ans += 1
        que.append((u, v))
print(ans)
