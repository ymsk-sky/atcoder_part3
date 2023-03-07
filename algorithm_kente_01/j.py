import heapq

h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]
INF = float("inf")
dist = [[[INF] * w for _ in range(h)] for _ in range(3)]
sl = ((h - 1, 0), (h - 1, w - 1), (0, w - 1))
for k in range(3):
    si, sj = sl[k]
    que = [(0, si, sj)]
    heapq.heapify(que)
    while que:
        cost, i, j = heapq.heappop(que)
        if dist[k][i][j] <= cost:
            continue
        dist[k][i][j] = cost
        for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            u, v = i + p, j + q
            if 0 > u or u >= h or 0 > v or v >= w:
                continue
            if dist[k][u][v] <= cost + al[u][v]:
                continue
            heapq.heappush(que, (cost + al[u][v], u, v))
ans = INF
for i in range(h):
    for j in range(w):
        tmp = dist[0][i][j] + dist[1][i][j] + dist[2][i][j] - 2*al[i][j]
        ans = min(ans, tmp)
print(ans)
