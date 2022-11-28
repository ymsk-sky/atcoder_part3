def modpow(a, n, mod):
    """a**n % mod を計算 O(log(n))
    """
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

n, q = map(int, input().split())
al = list(map(int, input().split()))
cl = list(map(int, input().split()))
mod = 10**9 + 7

# 距離を計算し累積和をとる
dl = [0]
for i in range(1, n):
    d = modpow(al[i - 1], al[i], mod)
    dl.append(d)
    dl[i] += dl[i - 1]
    dl[i] %= mod

ans = 0
bef = 1
for c in cl + [1]:
    crt = c
    if bef > crt:
        bef, crt = crt, bef
    d = dl[crt - 1] - dl[bef - 1]
    ans += d
    ans %= mod
    bef = c
print(ans)