from collections import deque

INF = float("inf")
while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    wall_h = []
    wall_w = []
    for i in range(2 * h - 1):
        l = list(map(int, input().split()))
        if i % 2 == 0:
            wall_h.append(l)
        else:
            wall_w.append(l)
    dist = [[INF] * w for _ in range(h)]
    dist[0][0] = 1

    q = deque()
    q.append((0, 0))
    while q:
        i, j = q.popleft()
        d = dist[i][j]
        # Left
        if j - 1 >= 0:
            if wall_h[i][j - 1] == 0:
                if dist[i][j - 1] > d + 1:
                    dist[i][j - 1] = d + 1
                    q.append((i, j - 1))
        # Right
        if j + 1 < w:
            if wall_h[i][j] == 0:
                if dist[i][j + 1] > d + 1:
                    dist[i][j + 1] = d + 1
                    q.append((i, j + 1))
        # Up
        if i - 1 >= 0:
            if wall_w[i - 1][j] == 0:
                if dist[i - 1][j] > d + 1:
                    dist[i - 1][j] = d + 1
                    q.append((i - 1, j))
        # Down
        if i + 1 < h:
            if wall_w[i][j] == 0:
                if dist[i + 1][j] > d + 1:
                    dist[i + 1][j] = d + 1
                    q.append((i + 1, j))
    ans = dist[h - 1][w - 1]
    print(0 if ans == INF else ans)