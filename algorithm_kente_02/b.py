s = input()
d = {c: s.count(c) for c in "abc"}
print(max(d, key=lambda e: d[e]))
