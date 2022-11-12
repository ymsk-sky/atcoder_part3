n, m = map(int, input().split())
dl = [int(input()) for _ in range(n)]
cl = [int(input()) for _ in range(m)]

INF = float("inf")

# dp[i][j]: i日目に都市jにいる場合のこれまでの最低累計疲労
dp = [[INF] * (n + 1) for _ in range(m + 1)]
for i in range(m - n + 1):
    dp[i][0] = 0

for i in range(1, m + 1):
    c = cl[i - 1]
    for j in range(1, n + 1):
        if i < j:
            # i日目にj(>i)に移動することは不可能
            break
        d = dl[j - 1]
        dp[i][j] = min(dp[i - 1][j - 1] + c * d,
                       dp[i - 1][j])

print(dp[m][n])