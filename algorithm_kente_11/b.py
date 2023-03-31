s = input()
d = dict()
for a, b in zip(s, s[1:]):
    w = a + b
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
n = max(d.values())
ans = []
for k in d:
    if d[k] == n:
        ans.append(k)
ans.sort()
print(ans[0])
