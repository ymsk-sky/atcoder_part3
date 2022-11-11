M = 10 ** 5
# 素数判定
f = [1] * (M + 1)
f[0] = f[1] = 0
for i in range(2, M + 1):
    if f[i]:
        for j in range(2 * i, M + 1, i):
            f[j] = 0
# i, (i+1)//2 共に素数かを判定
g = [0] * (M + 1)
for i in range(1, M + 1, 2):
    j = (i + 1) // 2
    if f[i] == 1 and f[j] == 1:
        g[i] = 1
# 累積和
for i in range(M):
    g[i + 1] += g[i]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    ans = g[r] - g[l - 1]
    print(ans)