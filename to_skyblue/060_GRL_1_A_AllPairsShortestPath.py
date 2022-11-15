INF = float("inf")
n, m = map(int, input().split())
edges = [[INF] * n for _ in range(n)]
for _ in range(m):
    s, t, d = map(int, input().split())
    edges[s][t] = d
for i in range(n):
    edges[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])
for i in range(n):
    if edges[i][i] < 0:
        print("NEGATIVE CYCLE")
        exit()
for edge in edges:
    print(*["INF" if v == INF else v for v in edge])