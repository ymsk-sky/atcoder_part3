n, k = map(int, input().split())
cl = list(map(int, input().split()))
pl = list(map(int, input().split()))
l = [(p, c) for c, p in zip(cl, pl)]
l.sort()

s = set()
ans = 0
for p, c in l:
    if c in s:
        continue
    s.add(c)
    ans += p
    k -= 1
    if k == 0:
        break

print(ans if k == 0 else -1)
