n, m = map(int, input().split())
INF = float("inf")
edges = [[INF] * n for _ in range(n)]
for _ in range(m):
    s, t, d = map(int, input().split())
    edges[s][t] = d

"""bitDP
dp[S][v]: 全体の集合のうちの部分集合Sの順列の中で, vが末項となるもののうちの最短経路.
このSをbitで表す
"""
dp = [[INF] * n for _ in range(1 << n)]  # 2 ** n == 1 << n
dp[0][0] = 0

for S in range(1 << n):
    for v in range(n):
        for u in range(n):
            if (S >> u) & 1 == 0 and S != 0:
                # u番目の頂点に訪れている,またはどこの頂点にも訪れていない場合は続ける
                continue
            if (S >> v) & 1 == 0:
                if dp[S | (1 << v)][v] > dp[S][u] + edges[u][v]:
                    dp[S | (1 << v)][v] = dp[S][u] + edges[u][v]

ans = dp[-1][0]
print(-1 if ans == INF else ans)
