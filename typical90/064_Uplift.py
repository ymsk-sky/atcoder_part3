n, q = map(int, input().split())
al = list(map(int, input().split()))
lrvl = [list(map(int, input().split())) for _ in range(q)]

if n == 1:
    print(*[0]*q, sep="\n")
    exit()

# 必要な情報は横との差だけ
dif = []  # dif[i]: [d1, d2]: 前との差,後との差(自分 - 相手)->自分が相手よりdn高い
for i in range(n):
    if i == 0:
        dif.append([0, al[i] - al[i + 1]])
    elif i == n - 1:
        dif.append([al[i] - al[i - 1], 0])
    else:
        dif.append([al[i] - al[i - 1], al[i] - al[i + 1]])

ans = sum([abs(a - b) for a, b in zip(al, al[1:])])
for l, r, v in lrvl:
    l, r = l - 1, r - 1
    # 左端処理
    bef_l = abs(dif[l][0])
    if l > 0:
        dif[l][0] += v
        dif[l - 1][1] -= v
    crt_l = abs(dif[l][0])
    # 右端処理
    bef_r = abs(dif[r][1])
    if r < n - 1:
        dif[r][1] += v
        dif[r + 1][0] -= v
    crt_r = abs(dif[r][1])
    ans += (crt_l + crt_r) - (bef_l + bef_r)

    print(ans)