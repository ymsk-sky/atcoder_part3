n, a = map(int, input().split())
xl = list(map(int, input().split()))

# dp[i][j][s]: i枚目まででj枚使って合計がsとなる組み合わせ
dp = [[[0] * (50*n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1
for i in range(1, n + 1):
    x = xl[i - 1]
    dp[i][0][0] = 1
    for j in range(1, n + 1):
        if i < j:
            continue
        for s in range(50*n + 1):
            # i枚目を使う
            dp[i][j][s] += dp[i - 1][j][s]
            # i枚目を使わない
            if s - x >= 0:
                dp[i][j][s] += dp[i - 1][j - 1][s - x]
ans = 0
for j in range(1, n + 1):
    if a*j > 50*n:
        break
    ans += dp[n][j][a*j]
print(ans)