import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for num in range(1, m + 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append((c, b, num))
    edges[b].append((c, a, num))
for i in range(n):
    edges[i] = sorted(edges[i])

INF = float("inf")

dist = [INF] * n
to = [-1] * n

que = []
heapq.heapify(que)
heapq.heappush(que, (0, 0, -1))
while que:
    d, crt, used = heapq.heappop(que)
    if dist[crt] != INF:
        continue
    dist[crt] = d
    to[crt] = used
    for cost, nxt, num in edges[crt]:
        if dist[nxt] > d + cost:
            # dist[nxt] = d + cost
            heapq.heappush(que, (d + cost, nxt, num))
print(*set(to[1:]))