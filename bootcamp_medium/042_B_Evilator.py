sl = input()
n = len(sl)
ans = 0
for i in range(1, n + 1):
    s = sl[i - 1]
    if s == "U":
        ans += (n - i) + 2*(i - 1)
    else:
        ans += (i - 1) + 2*(n - i)
print(ans)
