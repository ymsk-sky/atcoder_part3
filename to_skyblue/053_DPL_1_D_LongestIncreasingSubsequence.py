from bisect import bisect_left

n = int(input())
l = [int(input())]
for _ in range(n - 1):
    a = int(input())
    if a > l[-1]:
        l.append(a)
    else:
        ix = bisect_left(l, a)
        l[ix] = a
print(len(l))