from bisect import bisect_left

n = int(input())
sl = list(map(int, input().split()))
q = int(input())
tl = list(map(int, input().split()))

sl.sort()
ans = 0
for t in tl:
    ix = bisect_left(sl, t)
    if ix == n:
        continue
    if t == sl[ix]:
        ans += 1
print(ans)