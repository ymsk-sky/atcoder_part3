def factrization(n):
    """nを素因数分解する
    n = e1**p1 * e2**p2 * ... * em**pm
    を [(e1, p1), (e2, p2), ..., (em, pm)] で返す
    """
    ar = []
    tmp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp %i == 0:
                cnt += 1
                tmp //= i
            ar.append((i, cnt))
    if tmp != 1:
        ar.append((tmp, 1))
    if not ar:
        ar.append((n, 1))
    return ar

n = int(input())
al = list(map(int, input().split()))

fl = [[0, 0] for _ in range(n)]  # [2乗, 3乗]
kl = []  # その他
for i in range(n):
    f = factrization(al[i])
    for x, y in f:
        if x == 1:
            continue
        elif x == 2:
            fl[i][0] = y
        elif x == 3:
            fl[i][1] = y
        else:
            kl.append(x**y)
x2 = min(fl, key=lambda f: f[0])[0]
x3 = min(fl, key=lambda f: f[1])[1]

# すべての値を 2**x2 * 3**x3 * k0 * k1 * ... にする
ans = 0
for i in range(n):
    a = al[i]
    for k in kl:
        if a % k != 0:
            print(-1)
            exit()
    b, c = fl[i]
    ans += b - x2
    ans += c - x3
print(ans)