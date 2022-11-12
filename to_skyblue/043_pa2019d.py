n = int(input())
sl = [input() for _ in range(5)]

INF = float("inf")
col = "RBW"

# dp[i][j]: i列目を色jにするときの最低累計変化数
dp = [[INF] * 3 for _ in range(n + 1)]
dp[0] = [0, 0, 0]
for i in range(1, n + 1):
    l = [sl[k][i - 1] for k in range(5)]
    for j in range(3):
        c = col[j]
        cnt = 5 - l.count(c)
        dp[i][j] = min(dp[i - 1][(j + 1) % 3],
                       dp[i - 1][(j + 2) % 3]) + cnt

print(min(dp[n]))