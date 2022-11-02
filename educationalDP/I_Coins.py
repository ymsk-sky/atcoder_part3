n = int(input())
pl = list(map(float, input().split()))

# dp[i][j]: i枚目まででj枚が表になる確率
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    p = pl[i - 1]
    for j in range(i + 1):
        if j == 0:
            # 0 < j < iのときの第2項
            dp[i][j] = dp[i - 1][j] * (1 - p)
        elif j == i:
            # 0 < j < iのときの第1項
            dp[i][j] = dp[i - 1][j - 1] * p
        else:
            dp[i][j] = (dp[i - 1][j - 1] * p) + (dp[i - 1][j] * (1 - p))
print(sum(dp[n][-(-n // 2):]))
"""
1<=n<=2999, n%2=1
0<p<1
確率pで表,1-pで裏
表の数が裏の数を上回る確率

30%で起こる事象Aと40%で起こる事象Bにおいて
両方発生: 30% * 40% = 12%
両方不発: 70% * 60% = 42%
片方発生: 30% * 60% + 70% * 40% = 18% + 28% = 46%

3
0.30 0.60 0.80
0.612
"""
