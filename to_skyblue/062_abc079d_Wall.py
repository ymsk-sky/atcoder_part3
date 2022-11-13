import heapq

h, w = map(int, input().split())
cl = [list(map(int, input().split())) for _ in range(10)]
al = [list(map(int, input().split())) for _ in range(h)]

INF = float("inf")

# res[i]: iから1への最小値
res = [0] * 11
for i in range(10):
    dist = [INF] * 10
    dist[i] = 0
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, i))
    while q:
        d, crt = heapq.heappop(q)
        if d > dist[crt]:
            continue
        for nxt in range(10):
            d_nxt = cl[crt][nxt]
            tmp = d + d_nxt
            if tmp < dist[nxt]:
                dist[nxt] = tmp
                heapq.heappush(q, (tmp, nxt))
    res[i] = dist[1]

ans = 0
for i in range(h):
    for j in range(w):
        ans += res[al[i][j]]
print(ans)