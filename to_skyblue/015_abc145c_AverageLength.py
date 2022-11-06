n = int(input())
xyl = [list(map(int, input().split())) for _ in range(n)]

dist = [[0] * n for _ in range(n)]
for i in range(n):
    x1, y1 = xyl[i]
    for j in range(i + 1, n):
        x2, y2 = xyl[j]
        d = (x1 - x2) ** 2 + (y1 - y2) ** 2
        dist[i][j] = dist[j][i] = d ** 0.5
ans = sum([sum(dist[i]) for i in range(n)]) / n
print(ans)