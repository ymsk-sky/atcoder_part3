n, m = map(int, input().split())
xys = {tuple(map(int, input().split())) for _ in range(m)}

ans = 1
for i in range(1, 1 << n):
    l = []
    for shift in range(n):
        if (i >> shift) & 1:
            l.append(shift + 1)
    if len(l) < 2:
        continue
    l.sort()
    tmp = len(l)
    f = True
    for i in range(tmp):
        for j in range(i + 1, tmp):
            if not (l[i], l[j]) in xys:
                f = False
                break
        if not f:
            break
    else:
        ans = max(ans, tmp)
print(ans)