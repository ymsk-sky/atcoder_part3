d, n = map(int, input().split())
tl = [int(input()) for _ in range(d)]
abcl = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j][k]: (i+1)日目に服(j+1)を着る時(ひとつ前がk+1)の派手さの最大累計値
dp = [[[-1] * (n) for _ in range(n)] for _ in range(d)]
# dp初期条件(1日目に着れる服を着る)
t = tl[0]
for j in range(n):
    a, b, c = abcl[j]
    if a <= t <= b:
        dp[0][j] = [0] * n

for i in range(1, d):
    t = tl[i]
    for j in range(n):
        a, b, c = abcl[j]
        if a <= t <= b:
            for k in range(n):
                if max(dp[i - 1][k]) < 0:
                    continue
                dp[i][j][k] = max(dp[i - 1][k]) + abs(c - abcl[k][2])

print(max([max(p) for p in dp[d - 1]]))