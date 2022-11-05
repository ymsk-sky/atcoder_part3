n, k = map(int, input().split())
al = list(map(int, input().split()))

ans = float("inf")
for i in range(1 << n):
    # bitが立っているところが見えるようにする
    if bin(i).count("1") < k:
        continue
    tmp = 0
    crt = al[0]
    for j in range(1, n):
        if (i >> j) & 1 == 0:
            crt = max(crt, al[j])
        else:
            if crt >= al[j]:
                tmp += crt - al[j] + 1
                crt += 1
            else:
                crt = al[j]
    ans = min(ans, tmp)
print(ans)