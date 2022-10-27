n, k = map(int, input().split())
al = []
bl = []
for _ in range(n):
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)
r = max(*al, k) + 1
c = max(*bl, k) + 1
"""
ab平面の(k+1)*(k+1)の範囲に最も多く点が入る範囲
->二次元累積和
"""
f = [[0] * (c + 1) for _ in range(r + 1)]
for a, b in zip(al, bl):
    f[a][b] += 1

for i in range(1, r + 1):
    for j in range(1, c):
        f[i][j + 1] += f[i][j]
for j in range(1, c + 1):
    for i in range(1, r):
        f[i + 1][j] += f[i][j]

ans = 0
for i in range(r - k):
    for j in range(c - k):
        tmp = f[i][j] + f[i + k + 1][j + k + 1] - f[i][j + k + 1] - f[i + k + 1][j]
        ans = max(ans, tmp)
print(ans)