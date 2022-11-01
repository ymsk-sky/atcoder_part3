h, w = map(int, input().split())
a = [input() for _ in range(h)]
mod = 10 ** 9 + 7
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if j + 1 < w and a[i][j + 1] == ".":
            dp[i][j + 1] += dp[i][j]
            dp[i][j + 1] %= mod
        if i + 1 < h and a[i + 1][j] == ".":
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
print(dp[h - 1][w - 1])