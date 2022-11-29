"""
「現時点でコストが最も低い頂点に対して操作を行う」をn回繰り返す
他が消えたところでコストが増えることはない
"""
import heapq

n, m = map(int, input().split())
al = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)

que = []
heapq.heapify(que)
for crt in range(n):
    cost = 0
    for nxt in edges[crt]:
        cost += al[nxt]
    heapq.heappush(que, (cost, crt))

extracted = [0] * n
ans = 0
while que:
    tmp, pos = heapq.heappop(que)
    if extracted[pos]:
        continue
    extracted[pos] = 1
    ans = max(ans, tmp)

    for crt in edges[pos]:
        if extracted[crt]:
            continue
        cost = 0
        for nxt in edges[crt]:
            if extracted[nxt]:
                continue
            cost += al[nxt]
        heapq.heappush(que, (cost, crt))
print(ans)