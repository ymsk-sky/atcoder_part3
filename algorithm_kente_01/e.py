n, q = map(int, input().split())
f = [[0] * n for _ in range(n)]
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        a, b = s[1:]
        f[a - 1][b - 1] = 1
    elif s[0] == 2:
        a = s[1]
        for x in range(n):
            if f[x][a - 1]:
                f[a - 1][x] = 1
    else:
        a = s[1]
        g = f[a - 1].copy()
        for x in range(n):
            if f[a - 1][x]:
                for y in range(n):
                    if f[x][y] and (y + 1 != a):
                        g[y] = 1
        f[a - 1] = g[:]

for l in f:
    print(*["Y" if e else "N" for e in l], sep="")
