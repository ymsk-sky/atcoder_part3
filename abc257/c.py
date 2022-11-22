from bisect import bisect_left

n = int(input())
s = input()
wl = list(map(int, input().split()))

adult = []
child = []
for i in range(n):
    w = wl[i]
    if s[i] == "1":
        adult.append(w)
    else:
        child.append(w)
adult.sort()
child.sort()
la = len(adult)
lc = len(child)
ans = 0
for x in [0] + wl + [10**9 + 1]:
    tmp = 0
    # x以上を大人とす
    i = bisect_left(adult, x)
    tmp += (la - i)
    j = bisect_left(child, x)
    tmp += j
    ans = max(ans, tmp)
print(ans)