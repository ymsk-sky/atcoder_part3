n = int(input())
d = dict()
for _ in range(n):
    s = input()
    v = int(s)
    if v in d:
        d[v].append(s)
    else:
        d[v] = [s]

for k in sorted(d):
    for s in sorted(d[k], key=lambda e: len(e), reverse=True):
        print(s)
