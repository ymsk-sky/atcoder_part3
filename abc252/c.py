n = int(input())
sl = [input() for _ in range(n)]
ans = float("inf")
for x in range(10):
    # xを揃える
    tl = set()
    for s in sl:
        t = s.index(str(x))
        while t in tl:
            t += 10
        tl.add(t)
    tmp = max(tl)
    ans = min(ans, tmp)
print(ans)