s = input()
ans = float("inf")
n = len(s)
for a in range(ord("a"), ord("z") + 1):
    c = chr(a)
    t = s[:]
    tmp = 0
    while 1:
        if len(set(t)) == 1:
            break
        t = "".join([c if t[i + 1] == c else t[i] for i in range(n - tmp - 1)])
        tmp += 1
    ans = min(ans, tmp)
print(ans)
