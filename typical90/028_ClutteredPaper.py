"""自回答
2次元いもす法

左下(lx,ly), 右上(rx,ry)の範囲のとき
(lx,ly),(rx,ry): +1
(lx,ry),(rx,ly): -1
x軸 -> y軸の順で累積和をとる
"""
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
M = 1000

f = [[0] * (M + 1) for _ in range(M + 1)]

# 左下(lx,ly), 右上(rx,ry)
for lx, ly, rx, ry in l:
    f[lx][ly] += 1
    f[rx][ry] += 1
    f[lx][ry] -= 1
    f[rx][ly] -= 1

for i in range(M + 1):
    for j in range(M):
        f[i][j + 1] += f[i][j]
for j in range(M + 1):
    for i in range(M):
        f[i + 1][j] += f[i][j]

ans = [0] * (n + 1)
for i in range(M + 1):
    for j in range(M + 1):
        ans[f[i][j]] += 1
for k in range(1, n + 1):
    print(ans[k])