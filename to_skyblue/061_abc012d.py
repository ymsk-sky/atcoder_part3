import heapq

n, m = map(int, input().split())
INF = float("inf")
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    edges[a - 1].append((t, b - 1))
    edges[b - 1].append((t, a - 1))

ans = INF
for i in range(n):
    dist = [INF] * n
    dist[i] = 0

    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, i))

    while q:
        d, crt = heapq.heappop(q)
        if d > dist[crt]:
            continue
        for d_nxt, nxt in edges[crt]:
            tmp = d + d_nxt
            if tmp < dist[nxt]:
                dist[nxt] = tmp
                heapq.heappush(q, (tmp, nxt))
    res = max(dist)
    ans = min(ans, res)
print(ans)