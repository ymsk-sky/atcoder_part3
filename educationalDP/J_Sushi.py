"""
期待値DP
"""
n = int(input())
al = list(map(int, input().split()))

c = [0] * 4
for a in al:
    c[a] += 1

# dp[i][j][k]: 3個残りがi個, 2個残りがj個,1個残りがk個の状態にするまでの期待値
dp = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(n + 2)]

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            s = i + j + k
            if s == 0:
                continue
            dp[i][j][k] = n / s
            if i > 0:
                dp[i][j][k] += dp[i - 1][j + 1][k] * i / s
            if j > 0:
                dp[i][j][k] += dp[i][j - 1][k + 1] * j / s
            if k > 0:
                dp[i][j][k] += dp[i][j][k - 1] * k / s
print(dp[c[3]][c[2]][c[1]])