import heapq
from collections import deque

INF = float("inf")

n, m, k, s = map(int, input().split())
p, q = map(int, input().split())
danger = [INF] * n  # 支配された町との距離を記録する
que = deque()
for _ in range(k):
    c = int(input())
    danger[c - 1] = 0  # 支配された町
    que.append(c - 1)
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

# 支配された町との距離を探索
while que:
    crt = que.popleft()
    for nxt in edges[crt]:
        if danger[nxt] != INF:
            continue
        danger[nxt] = danger[crt] + 1
        que.append(nxt)

# 町0->町(n-1)を最安値で移動
dist = [INF] * n
dist[0] = 0
que = []
heapq.heapify(que)
for edge in edges[0]:
    cost = p if danger[edge] > s else q  # 支配された町との距離に応じて宿泊費を決定
    heapq.heappush(que, (cost ,edge))
while que:
    cost, crt = heapq.heappop(que)
    for nxt in edges[crt]:
        if dist[nxt] != INF or danger[nxt] == 0:
            continue
        nxt_cost = p if danger[nxt] > s else q
        dist[nxt] = cost + nxt_cost
        heapq.heappush(que, (dist[nxt], nxt))

ans = INF
for edge in edges[n - 1]:
    if danger[edge] == 0:
        continue
    ans = min(ans, dist[edge])
print(ans)

"""
2<=n<=10**5
1<=m<=2*10**5
0<=k<=n-2
0<=s<=10**5

1<=p<q<=10**5
2<=c<=n-1
1<=a<b<=n
"""
