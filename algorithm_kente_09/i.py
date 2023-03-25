import heapq
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
d[1].append((n - 1, n))
d[n].append((n - 1, 1))
for _ in range(m):
    a, b, c = map(int, input().split())
    d[a].append((c, b))
    d[b].append((c, a))

kl = sorted(d.keys())
for k1, k2 in zip(kl, kl[1:]):
    d[k1].append((k2 - k1, k2))
    d[k2].append((k2 - k1, k1))

INF = float("inf")
dist = {k: INF for k in kl}

que = [(0, 1)]
heapq.heapify(que)
while que:
    cost, crt = heapq.heappop(que)
    if dist[crt] <= cost:
        continue
    dist[crt] = cost
    for nxt_cost, nxt in d[crt]:
        if dist[nxt] <= cost + nxt_cost:
            continue
        heapq.heappush(que, (cost + nxt_cost, nxt))

print(dist[n])
