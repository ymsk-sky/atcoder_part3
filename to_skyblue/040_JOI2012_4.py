n, k = map(int, input().split())
abl = [[1, 2, 3]] * n
for _ in range(k):
    a, b = map(int, input().split())
    abl[a - 1] = [b]
# abl = [list(map(int, input().split())) for _ in range(k)]
mod = 10_000

# dp[i][j][k]: (i+1)日目に(j+1)を食べる(連続k+1回目)の組み合わせ
dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
for j in abl[0]:
    dp[0][j - 1][0] = 1

for i in range(1, n):
    for j in abl[i]:
        dp[i][j - 1][0] = (dp[i - 1][j % 3][0] + dp[i - 1][j % 3][1] +
                           dp[i - 1][(j + 1) % 3][0] +
                           dp[i - 1][(j + 1) % 3][1])
        dp[i][j - 1][0] %= mod
        dp[i][j - 1][1] = dp[i - 1][j - 1][0]
        dp[i][j - 1][1] %= mod

print(sum([sum(v) for v in dp[n - 1]]) % mod)