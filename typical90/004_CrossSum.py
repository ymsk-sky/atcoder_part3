h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]

shl = [sum(l) for l in al]
swl = [sum([al[i][j] for i in range(h)]) for j in range(w)]

bl = []
for i in range(h):
    tmp = []
    for j in range(w):
        b = shl[i] + swl[j] - al[i][j]
        tmp.append(b)
    bl.append(tmp)

for l in bl:
    print(*l)