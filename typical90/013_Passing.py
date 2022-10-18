from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
for i in range(1, n + 1):
    edges[i] = sorted(edges[i], key=lambda e: e[1])

INF = float("inf")

dist1 = [INF] * (n + 1)
dist1[1] = 0
dist2 = [INF] * (n + 1)
dist2[n] = 0

# 1->k(1<=k<=n)の最短経路探索
q = deque([1])
while q:
    crt = q.popleft()
    for nxt, cost in edges[crt]:
        if dist1[nxt] > dist1[crt] + cost:
            dist1[nxt] = dist1[crt] + cost
            q.append(nxt)

# n->k(1<=k<=n)すなわちk->nの最短経路探索
q = deque([n])
while q:
    crt = q.popleft()
    for nxt, cost in edges[crt]:
        if dist2[nxt] > dist2[crt] + cost:
            dist2[nxt] = dist2[crt] + cost
            q.append(nxt)

for k in range(1, n + 1):
    # 1->k->nの最短距離
    print(dist1[k] + dist2[k])