from collections import deque

h, w = map(int, input().split())
s = [input() for _ in range(h)]

dist = [[-1] * w for _ in range(h)]
dist[0][0] = 0

q = deque()
q.append((0, 0))
while q:
    y, x = q.popleft()
    for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= y + i < h and 0 <= x + j < w:
            if s[y + i][x + j] == "#" or dist[y + i][x + j] >= 0:
                continue
            dist[y + i][x + j] = dist[y][x] + 1
            q.append((y + i, x + j))

if dist[h - 1][w - 1] == -1:
    print(-1)
else:
    cnt = dist[h - 1][w - 1] + 1
    wall = sum([l.count("#") for l in s])
    ans = h * w - (cnt + wall)
    print(ans)