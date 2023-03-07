n, m = map(int, input().split())
sl = []
cl = []
for _ in range(m):
    s, c = input().split()
    sl.append(sum([1<<i for i in range(n) if s[i] == "Y"]))
    cl.append(int(c))
INF = float("inf")
dp = [INF] * (1<<n)
dp[0] = 0
for i in range(1<<n):
    for j in range(m):
        dp[i | sl[j]] = min(dp[i | sl[j]], dp[i] + cl[j])
ans = dp[-1]
print(-1 if ans == INF else ans)
