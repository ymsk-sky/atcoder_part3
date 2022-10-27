from bisect import bisect_left

n = int(input())
s = input()

xl = []
ol = []
for i in range(n):
    if s[i] == "x":
        xl.append(i)
    else:
        ol.append(i)

ans = 0
for i in range(n):
    if s[i] == "x":
        ix = bisect_left(ol, i)
        m = n if ix == len(ol) else ol[ix]
    else:
        ix = bisect_left(xl, i)
        m = n if ix == len(xl) else xl[ix]
    ans += n - m
print(ans)