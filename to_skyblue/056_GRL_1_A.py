import heapq

n, m, r = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    s, t, d = map(int, input().split())
    graph[s].append([d, t])
INF = float("inf")

dist = [INF] * n

q = []
heapq.heapify(q)
heapq.heappush(q, [0, r])
while q:
    cost, crt = heapq.heappop(q)
    if dist[crt] < cost:
        continue
    dist[crt] = cost
    for nxt_cost, nxt in graph[crt]:
        if dist[nxt] < dist[crt] + nxt_cost:
            continue
        heapq.heappush(q, [dist[crt] + nxt_cost, nxt])

print(*["INF" if d == INF else d for d in dist], sep="\n")