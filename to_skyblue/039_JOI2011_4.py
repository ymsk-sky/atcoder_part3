n = int(input())
l = list(map(int, input().split()))

# dp[i][j]: (i+1)個目まででj(0<=j<=20)になる個数
dp = [[0] * 21 for _ in range(n)]
dp[1][l[0]] = 1
for i in range(2, n):
    num = l[i - 1]
    for j in range(21):
        # +num
        if j - num >= 0:
            dp[i][j] += dp[i - 1][j - num]
        # -num
        if j + num <= 20:
            dp[i][j] += dp[i - 1][j + num]
print(dp[n - 1][l[-1]])