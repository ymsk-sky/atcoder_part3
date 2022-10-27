l, r = map(int, input().split())
mod = 10 ** 9 + 7

kl = len(str(l))
kr = len(str(r))
ans = 0
for k in range(kl, kr + 1):
    if k == kl:
        a = l
    else:
        a = 10 ** (k - 1)

    if k == kr:
        b = r
    else:
        b = int("9" * k)
    tmp = k * (a + b) * (b - a + 1) // 2 % mod
    ans += tmp
    ans %= mod
print(ans)