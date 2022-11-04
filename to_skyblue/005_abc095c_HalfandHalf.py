a, b, c, x, y = map(int, input().split())
ans = float("inf")
for z in range(0, 2 * 10 ** 5 + 1, 2):
    z2 = z // 2
    rx = max(0, x - z2)
    ry = max(0, y - z2)
    tmp = a * rx + b * ry + c * z
    ans = min(ans, tmp)
print(ans)