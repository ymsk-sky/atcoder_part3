import heapq

n, k = map(int, input().split())
ll = [list(map(int, input().split())) for _ in range(k)]

INF = float("inf")

edges = [[] for _ in range(n)]

def dijkstra(a, b):
    # 距離
    dist = [INF] * n
    dist[a] = 0

    q = []
    heapq.heapify(q)
    for edge in edges[a]:
        heapq.heappush(q, edge)
    
    while q:
        cost, crt = heapq.heappop(q)
        if dist[crt] != INF:
            continue
        dist[crt] = cost
        for nxt_cost, nxt in edges[crt]:
            if dist[nxt] != INF:
                continue
            heapq.heappush(q, (dist[crt] + nxt_cost, nxt))
    
    ans = dist[b]
    return ans if ans != INF else -1


for l in ll:
    if l[0] == 0:
        # 注文票: a->b
        _, a, b = l
        ans = dijkstra(a - 1, b - 1)
        print(ans)
    else:
        # 新たな運行情報: c-d間の運賃がe
        _, c, d, e = l
        edges[c - 1].append((e, d - 1))
        edges[d - 1].append((e, c - 1))

"""
1<=n<=100
1<=k<=5000

1<=a,b<=n
1<=c,d<=n
1<=e<=10**6
"""