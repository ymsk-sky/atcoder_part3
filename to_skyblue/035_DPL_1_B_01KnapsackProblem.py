N, W = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i個目までで重さがjとなるときの最大価値
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    v, w = l[i - 1]
    for j in range(W + 1):
        dp[i][j] = dp[i - 1][j]
        if j - w >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
print(dp[N][W])