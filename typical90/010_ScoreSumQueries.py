from bisect import bisect_left
from itertools import accumulate

n = int(input())
cpl = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
lrl = [list(map(int, input().split())) for _ in range(q)]

# 点数
ap = []
bp = []
# 学籍番号
an = []
bn = []
for i in range(1, n + 1):
    c, p = cpl[i - 1]
    if c == 1:
        ap.append(p)
        an.append(i)
    else:
        bp.append(p)
        bn.append(i)

aca = [0] + list(accumulate(ap))
acb = [0] + list(accumulate(bp))

for l, r in lrl:
    il = bisect_left(an, l)
    ir = bisect_left(an, r)
    if il == len(an):
        ans_a = 0
    else:
        acl = aca[il]
        if ir == len(an):
            acr = aca[ir]
        else:
            if r == an[ir]:
                acr = aca[ir + 1]
            else:
                acr = aca[ir]
        ans_a = acr - acl

    jl = bisect_left(bn, l)
    jr = bisect_left(bn, r)
    if jl == len(bn):
        ans_b = 0
    else:
        acl = acb[jl]
        if jr == len(bn):
            acr = acb[jr]
        else:
            if r == bn[jr]:
                acr = acb[jr + 1]
            else:
                acr = acb[jr]
        ans_b = acr - acl

    print(ans_a, ans_b)