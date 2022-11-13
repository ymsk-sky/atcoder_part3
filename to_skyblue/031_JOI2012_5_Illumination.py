from collections import deque

w, h = map(int, input().split())
c = [[0] * (w + 2)]
for _ in range(h):
    l = list(map(int, input().split()))
    c.append([0] + l + [0])
c.append([0] * (w + 2))

h, w = h + 2, w + 2
# 建物の外側を探索
ol = [[0] * w for _ in range(h)]
ol[0][0] = 1

q = deque()
q.append((0, 0))

l = (((-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)),
     ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)))
while q:
    i, j = q.popleft()
    for nxt in l[i % 2]:
        u = i + nxt[0]
        v = j + nxt[1]
        if 0 <= u < h and 0 <= v < w:
            if c[u][v] == 1 or ol[u][v] == 1:
                continue
            ol[u][v] = 1
            q.append((u, v))

ans = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == 1 or ol[i][j] == 0:
            continue
        for nxt in l[i % 2]:
            u = i + nxt[0]
            v = j + nxt[1]
            if 0 <= u < h and 0 <= v < w:
                if c[u][v] == 1:
                    ans += 1
print(ans)
