n = int(input())
s = input()
mod = 10 ** 9 + 7
a = "atcoder"

# dp[i][j]: i文字目までにa[:j]までか完成する組み合わせ数 % mod
dp = [[0] * 8 for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    c = s[i - 1]
    for j in range(1, 8):
        if i < j:
            continue
        if c == a[j - 1]:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j]
        dp[i][j] %= mod

print(dp[n][7])