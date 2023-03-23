n = int(input())
l = dict()
for _ in range(n):
    d, s, t = map(int, input().split())
    if d in l:
        l[d].append((s, t))
    else:
        l[d] = [(s, t)]
for k in l:
    now = 0
    for s, t in sorted(l[k]):
        if now > s:
            print("Yes")
            exit()
        now = t
print("No")
