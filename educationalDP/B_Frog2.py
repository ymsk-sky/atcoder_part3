n, k = map(int, input().split())
hl = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    ans = float("inf")
    for j in range(1, k + 1):
        if i - j >= 0:
            ans = min(ans, dp[i - j] + abs(hl[i - j] - hl[i]))
    dp[i] = ans

print(dp[n - 1])
