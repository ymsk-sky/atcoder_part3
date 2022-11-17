INF = float("inf")
n = int(input())
dp = [[0] * 5 for _ in range(10**5 + 1)]
for _ in range(n):
    t, x, a = map(int, input().split())
    dp[t][x] = a
dp[0] = [0] + [-INF] * 4
for i in range(1, 10**5 + 1):
    for j in range(5):
        dp[i][j] += max(dp[i - 1][max(0, j - 1)],
                        dp[i - 1][j],
                        dp[i - 1][min(4, j + 1)])
print(max(dp[-1]))