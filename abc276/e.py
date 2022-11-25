from collections import deque

h, w = map(int, input().split())
c = [input() for _ in range(h)]

si, sj = 0, 0
for i in range(h):
    for j in range(w):
        if c[i][j] == "S":
            si, sj = i, j

visited = [[0] * w for _ in range(h)]

wl = ((-1, 0), (0, -1), (0, 1), (1, 0))
for k in range(4):
    fi, fj = si + wl[k][0], sj + wl[k][1]
    if 0 <= fi < h and 0 <= fj < w:
        if c[fi][fj] == "#":
            continue
    else:
        continue
    que = deque()
    que.append((fi, fj))
    while que:
        i, j = que.popleft()
        if visited[i][j] == k + 1:
            continue
        visited[i][j] = k + 1
        for u, v in wl:
            p, q = i + u, j + v
            if 0 <= p < h and 0 <= q < w:
                if c[p][q] == ".":
                    if visited[p][q] == k + 1:
                        continue
                    if visited[p][q] > 0:
                        print("Yes")
                        exit()
                    que.append((p, q))
print("No")