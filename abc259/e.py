n = int(input())
ll = []
for _ in range(n):
    m = int(input())
    l = [list(map(int, input().split())) for _ in range(m)]  # (p,e): p**e
    ll.append(l)

d = dict()
for l in ll:
    for p, e in l:
        if p in d:
            d[p].append(e)
        else:
            d[p] = [e]
for k in d:
    d[k] = sorted(d[k])

ans = set()
for l in ll:
    tmp = []
    for p, e in l:
        if d[p][-1] == e:
            if len(d[p]) == 1:
                tmp.append((p, e))
            else:
                bef_e = d[p][-2]
                if bef_e != e:
                    tmp.append((p, e - bef_e))
        else:
            pass
    if tmp:
        ans.add(tuple(tmp))
    else:
        ans.add(((1, 1),))
print(len(ans))