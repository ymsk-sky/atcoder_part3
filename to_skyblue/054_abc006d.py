from bisect import bisect_left

n = int(input())
cl = [int(input()) for _ in range(n)]
l = [cl[0]]
for c in cl[1:]:
    if c > l[-1]:
        l.append(c)
    else:
        ix = bisect_left(l, c)
        l[ix] = c
print(n - len(l))