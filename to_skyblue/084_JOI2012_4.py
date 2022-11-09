n, m = map(int, input().split())
abxl = [list(map(int, input().split())) for _ in range(m)]
l = [[0] * (i + 2) for i in range(n + 1)]
o = [[0] * (i + 2) for i in range(n + 1)]
for a, b, x in abxl:
    l[a - 1][b - 1] += 1
    l[a - 1 + x + 1][b - 1] -= 1
    o[a - 1][b] += 1
    o[a - 1 + x + 1][b - 1 + x + 1 + 1] -= 1
for j in range(n):
    for i in range(j, n):
        l[i + 1][j] += l[i][j]
for i in range(n):
    for j in range(n - i):
        o[i + j + 1][j + 1] += o[i + j][j]

p = [[0] * (i + 2) for i in range(n + 1)]
for i in range(n + 1):
    for j in range(i + 2):
        p[i][j] = l[i][j] - o[i][j]

for i in range(n + 1):
    for j in range(i + 1):
        p[i][j + 1] += p[i][j]

ans = 0
for i in range(n):
    for j in range(i + 1):
        if p[i][j] > 0:
            ans += 1
print(ans)