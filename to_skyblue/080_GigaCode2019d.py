h, w, k, v = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]

ac = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        ac[i][j] = ac[i][j - 1] + al[i - 1][j - 1]
for j in range(1, w + 1):
    for i in range(1, h + 1):
        ac[i][j] += ac[i - 1][j]

ans = 0
for i1 in range(1, h + 1):
    for j1 in range(1, w + 1):
        for i2 in range(i1, h + 1):
            for j2 in range(j1, w + 1):
                s = (i2 - i1 + 1) * (j2 - j1 + 1)
                tmp = ac[i2][j2] + ac[i1 - 1][j1 - 1] - ac[i2][j1 - 1] - ac[i1 - 1][j2]
                if tmp + s * k <= v:
                    ans = max(ans, s)
print(ans)