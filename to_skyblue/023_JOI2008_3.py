from bisect import bisect_left

n, m = map(int, input().split())
pl = [int(input()) for _ in range(n)] + [0]  # 投げない=0点
n += 1

pp = set()
for i in range(n):
    for j in range(n):
        pp.add(pl[i] + pl[j])
pp = tuple(sorted(pp))
l = len(pp)

ans = 0
for p1 in pp:
    if p1 > m:
        break
    ix = min(bisect_left(pp, m - p1), l - 1)
    if pp[ix] > m - p1:
        p2 = pp[ix - 1]
    else:
        p2 = pp[ix]
    s = p1 + p2
    ans = max(ans, s)
print(ans)