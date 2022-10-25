n = int(input())
xyl = [list(map(int, input().split())) for _ in range(n)]

xl = []
yl = []
for x, y in xyl:
    xl.append(x)
    yl.append(y)

xl.sort()
yl.sort()

p = xl[n // 2]
q = yl[n // 2]

ans = 0
for x, y in zip(xl, yl):
    ans += abs(p - x)
    ans += abs(q - y)
print(ans)