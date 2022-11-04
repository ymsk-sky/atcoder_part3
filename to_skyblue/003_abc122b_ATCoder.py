s = input()
n = len(s)
ans = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        t = s[i:j]
        if len(set(t) - set("ACGT")) == 0:
            ans = max(ans, len(t))
print(ans)