n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

INF = float("inf")
dp = [[INF] * n for _ in range(n)]
for i in range(n):
    x1, y1, p1 = l[i]
    dp[i][i] = 0
    for j in range(i + 1, n):
        x2, y2, p2 = l[j]
        d = abs(x2 - x1) + abs(y2 - y1)
        s1 = -(-d // p1)
        dp[i][j] = s1
        s2 = -(-d // p2)
        dp[j][i] = s2

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], max(dp[i][k], dp[k][j]))

ans = INF
for i in range(n):
    tmp = max(dp[i])
    ans = min(ans, tmp)
print(ans)