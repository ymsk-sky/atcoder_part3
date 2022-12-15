n, k, m = map(int, input().split())
mod = 998244353

def modpow(p, e, mod):
    """p**e % mod"""
    res = 1
    while e > 0:
        if e & 1:
            res *= p%mod
        p = p*p%mod
        e >>= 1
    return res

# m**(k**n)はmの倍数のためm%mod=0なら答えも0になる
if m % mod == 0:
    print(0)
    exit()

"""
以下, mはpの倍数ではない
modは素数なのでフェルマーの定理より
m ** (mod-1) = 1 MOD mod
よってk**nを(mod-1)で割った商,余りをq,rとおくと
m**(k**n) = m**(q*(mod-1) + r) = (m**(mod-1))**q * m**r
= 1**q * m**r (MOD mod)
= 1 * m**r (MOD mod)
= m**r (MOD mod)

よってm**(k**n) MOD modはm**r MOD modと等しいので
答えを導くには
- k**n MOD (mod-1)
- m**r MOD mod
がわかればよい
"""

ans = modpow(k, n, mod - 1)
ans = modpow(m, ans, mod)
print(ans % mod)