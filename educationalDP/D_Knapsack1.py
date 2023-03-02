N, W = map(int, input().split())
wl, vl = [], []
for _ in range(N):
    w, v = map(int, input().split())
    wl.append(w)
    vl.append(v)
# dp[i][j]: i番目までで重さjのときの最大価値
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    w, v = wl[i - 1], vl[i - 1]
    for j in range(W + 1):
        dp[i][j] = dp[i - 1][j]
        if j - w >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
print(max(dp[N]))
