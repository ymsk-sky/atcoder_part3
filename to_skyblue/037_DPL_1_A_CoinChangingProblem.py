n, m = map(int, input().split())
cl = list(map(int, input().split()))

INF = float("inf")

# dp[i][j]: i番目まででj円のときの最小枚数
dp = [[INF] * (n + 1) for _ in range(m + 1)]
dp[0][0] = 0
for i in range(1, m + 1):
    c = cl[i - 1]
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j]
        if j - c >= 0:
            dp[i][j] = min(dp[i][j], dp[i][j - c] + 1)
print(dp[m][n])