"""
n回の行動をそれぞれx,y,z回行う場合でdpにする
n=x+y+zよりx,yが決まればzも決まる
"""
n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())
mod = 998244353
s = set(tuple(map(int, input().split())) for _ in range(m))

dp = [[[0] * 301 for _ in range(301)] for _ in range(301)]
dp[0][0][0] = 1

for i in range(1, n + 1):
    for x in range(n + 1):
        for y in range(n + 1):
            if x + y > i:
                break
            z = i - (x + y)

            pos = (a*x + c*y + e*z, b*x + d*y + f*z)
            if pos in s:
                continue

            dp[x][y][z] += dp[x - 1][y][z]
            dp[x][y][z] %= mod
            dp[x][y][z] += dp[x][y - 1][z]
            dp[x][y][z] %= mod
            dp[x][y][z] += dp[x][y][z - 1]
            dp[x][y][z] %= mod

ans = 0
for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            if x + y + z == n:
                ans += dp[x][y][z]
                ans %= mod
print(ans)