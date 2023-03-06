s = input()
d = []
w = []
f = 0
for c in s:
    w.append(c)
    if c.isupper():
        if f:
            d.append(("".join(w), "".join([x.lower() for x in w])))
            w = []
        f = 1 - f
d.sort(key=lambda e: e[1])
print(*[e[0] for e in d], sep="")
