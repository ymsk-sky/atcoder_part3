n, m = map(int, input().split())
s = [input() for _ in range(n)]
ans = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        cnt = 0
        for p in (-1, 0, 1):
            for q in (-1, 0, 1):
                u, v = i + p, j + q
                if 0 > u or u >= n or 0 > v or v >= m:
                    continue
                if s[u][v] == "#":
                    cnt += 1
        ans[i][j] = cnt

for an in ans:
    print(*an, sep="")
