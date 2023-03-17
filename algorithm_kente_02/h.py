import heapq

n, m = map(int, input().split())
al = [input() for _ in range(n)]

si = sj = gi = gj = -1
for i in range(n):
    for j in range(m):
        if al[i][j] == "S":
            si, sj = i, j
        if al[i][j] == "G":
            gi, gj = i, j

INF = float("inf")
dist = [[[INF] * 10 for _ in range(m)] for _ in range(n)]

que = [(0, si, sj, 0)]
heapq.heapify(que)
while que:
    d, i, j, k = heapq.heappop(que)
    if dist[i][j][k] <= d:
        continue
    dist[i][j][k] = d
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if 0 > u or u >= n or 0 > v or v >= m:
            continue
        if dist[u][v][k] > d + 1:
            heapq.heappush(que, (d + 1, u, v, k))
        if k < 9:
            if al[u][v] in "SG":
                continue
            if int(al[u][v]) == k + 1 and dist[u][v][k + 1] > d + 1:
                heapq.heappush(que, (d + 1, u, v, k + 1))

ans = dist[gi][gj][9]
print(-1 if ans == INF else ans)

"""
3 4
1S23
4567
89G1
"""
