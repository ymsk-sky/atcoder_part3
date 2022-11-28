# a**n % mod を計算 O(log(n))
def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

mod = 10**9 + 7
m, n = map(int, input().split())
print(modpow(m, n, mod))