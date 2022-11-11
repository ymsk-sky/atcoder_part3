from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [input() for _ in range(r)]

dist = [[-1] * c for _ in range(r)]
dist[sy - 1][sx - 1] = 0
q = deque()
q.append((sy - 1, sx - 1))

while q:
    y, x = q.popleft()
    for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if maze[y + i][x + j] == "#":
            continue
        if dist[y + i][x + j] > -1:
            continue
        dist[y + i][x + j] = dist[y][x] + 1
        q.append((y + i, x + j))

print(dist[gy - 1][gx - 1])