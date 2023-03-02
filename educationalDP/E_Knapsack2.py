N, W = map(int, input().split())
wl, vl = [], []
for _ in range(N):
    w, v = map(int, input().split())
    wl.append(w)
    vl.append(v)
M = 10**3
INF = float("inf")
# dp[i][j]: i番目までで価値がjのときの最小重さ
dp = [[INF] * (N*M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    w, v = wl[i - 1], vl[i - 1]
    for j in range(N*M + 1):
        dp[i][j] = dp[i - 1][j]
        if j - v >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - v] + w)
ans = 0
for j in range(N*M + 1):
    if dp[N][j] <= W:
        ans = j
print(ans)
