from collections import deque

n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n):
    u, k, *l = map(int, input().split())
    edges[u - 1] = l

INF = float("inf")

dist = [INF] * n
dist[0] = 0

q = deque()
q.append(1)

while q:
    crt = q.popleft()
    for nxt in edges[crt - 1]:
        if dist[nxt - 1] > dist[crt - 1] + 1:
            dist[nxt - 1] = dist[crt - 1] + 1
            q.append(nxt)

for i in range(n):
    if dist[i] == INF:
        dist[i] = -1
    print(i + 1, dist[i])
