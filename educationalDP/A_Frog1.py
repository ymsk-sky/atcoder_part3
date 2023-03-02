n = int(input())
hl = list(map(int, input().split()))

dp = [0] * n
dp[1] = abs(hl[0] - hl[1])
for i in range(2, n):
    dp[i] = min(dp[i - 2] + abs(hl[i - 2] - hl[i]),
                dp[i - 1] + abs(hl[i - 1] - hl[i]))
print(dp[n - 1])
