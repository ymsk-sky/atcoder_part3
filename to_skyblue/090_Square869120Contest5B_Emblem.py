n, m = map(int, input().split())
xyr_n = [list(map(int, input().split())) for _ in range(n)]
xy_m = [list(map(int, input().split())) for _ in range(m)]

INF = float("inf")

tmp0 = INF
for _, _, r in xyr_n:
    tmp0 = min(tmp0, r)

tmp1 = INF
for i in range(m):
    x1, y1 = xy_m[i]
    for j in range(i + 1, m):
        x2, y2 = xy_m[j]
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        d /= 2
        tmp1 = min(tmp1, d)

tmp2 = INF
for i in range(m):
    x1, y1 = xy_m[i]
    for x2, y2, r in xyr_n:
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 - r
        tmp2 = min(tmp2, d)

print(min(tmp1, tmp2, tmp0))