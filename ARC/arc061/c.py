s = input()
n = len(s)
ans = 0
for b in range(1 << (n - 1)):
    t = ["+" if (b >> i) & 1 else "" for i in range(n - 1)] + [""]
    ans += eval("".join([x+y for x, y in zip(s, t)]))
print(ans)