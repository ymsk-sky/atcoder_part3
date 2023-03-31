n, m = map(int, input().split())
ans = []
v = 1
f = 0
for k in range(m):
    if f:
        ans.append("x")
    else:
        v *= n
        if v > 10**9:
            ans.append("x")
            f = 1
        else:
            ans.append("o")
print(*ans, sep="")
