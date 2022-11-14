n, m = map(int, input().split())
INF = float("inf")
edges = [[[INF, INF] for _ in range(n)] for _ in range(n)]
for _ in [0] * m:
    s, t, d, time = map(int, input().split())
    s, t = s - 1, t - 1
    edges[s][t] = [d, time]
    edges[t][s] = [d, time]

# dp[S][v]: 集合Sでvが末項となるものの最短経路(Sはbitで表す), 経路数
dp = [[[INF, INF] for _ in range(n)] for _ in range(1 << n)]
# 最短経路距離0, 経路数1で初期化
dp[0][0] = [0, 1]
for S in range(1 << n):
    for v in range(n):
        for u in range(n):
            if (S >> u) & 1 == 0 and S != 0:
                continue
            # uに訪れている or どこにも訪れていない場合
            if (S >> v) & 1 == 0:
                if dp[S | (1 << v)][v][0] > dp[S][u][0] + edges[u][v][0]:
                    if edges[u][v][1] < dp[S][u][0] + edges[u][v][0]:
                        # 道路を渡り切るまでに閉鎖する場合は通れない
                        continue
                    dp[S | (1 << v)][v][0] = dp[S][u][0] + edges[u][v][0]
                    dp[S | (1 << v)][v][1] = dp[S][u][1]
                elif dp[S | (1 << v)][v][0] == dp[S][u][0] + edges[u][v][0]:
                    if edges[u][v][1] < dp[S][u][0] + edges[u][v][0]:
                        continue
                    # 最短経路距離が過去のものと同じときにその経路数を足す
                    dp[S | (1 << v)][v][1] += dp[S][u][1]

dist, num = dp[-1][0]
if dist == INF:
    print("IMPOSSIBLE")
else:
    print(dist, num)