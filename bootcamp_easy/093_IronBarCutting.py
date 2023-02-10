n = int(input())
al = list(map(int, input().split()))
ans = float("inf")
l = sum(al)
r = 0
for a in al:
    l -= a
    r += a
    dif = abs(l - r)
    ans = min(ans, dif)
print(ans)
