n, s = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: i個目まででjになるときの組み合わせ
dp = [[-1] * (s + 1) for _ in range(n + 1)]
a, b = abl[0]
if a <= s:
    dp[1][a] = 1
if b <= s:
    dp[1][b] = 0

for i in range(2, n + 1):
    a, b = abl[i - 1]
    for j in range(1, s + 1):
        if 0 < j - a <= s and dp[i - 1][j - a] >= 0:
            dp[i][j] = (dp[i - 1][j - a] << 1) + 1
        if 0 < j - b <= s and dp[i - 1][j - b] >= 0:
            dp[i][j] = (dp[i - 1][j - b] << 1) + 0

ans = dp[n][s]
if ans < 0:
    print("Impossible")
else:
    print(*["A" if (ans >> i) & 1 == 1 else "B" for i in range(n)][::-1], sep="")