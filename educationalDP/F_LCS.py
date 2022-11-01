s = input()
t = input()
n = len(s)
m = len(t)

# dp[i][j]: sのi文字目まででtのi文字目までとの最長の文字列長
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    c = s[i - 1]
    for j in range(1, m + 1):
        d = t[j - 1]
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        if c == d:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

l = dp[n][m]
ans = []
i = n
j = m
while l > 0:
    if s[i - 1] == t[j - 1]:
        ans.append(s[i - 1])
        i -= 1
        j -= 1
        l -= 1
    elif dp[i][j] == dp[i - 1][j]:
        i -= 1
    else:
        j -= 1
print(*ans[::-1], sep="")