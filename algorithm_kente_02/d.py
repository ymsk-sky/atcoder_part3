import re

f = [chr(i) for i in range(97, 123)] + [".", ""]
s = input()
l = set()
for i in range(28):
    for j in range(28):
        for k in range(28):
            w = "".join([f[i], f[j], f[k]])
            if w:
                l.add(w)

ans = 0
for w in l:
    if not re.search(w, s) is None:
        ans += 1
print(ans)
