"""
選べる色は
1. k種類
2. 1以外の(k-1)種類
3. 1,2以外の(k-2)種類
4. 2,3以外の(k-2)種類
...
n. (n-2),(n-1)以外の(k-2)種類
よｒって組み合わせは, k * (k - 1) * (k - 2) ** (n - 1)

これを, 繰り返し二乗法により a ** b mod m を高速に行うことで求める
"""
n, k = map(int, input().split())
mod = 10 ** 9 + 7

def f(a, b):
    ans = 1
    while b != 0:
        if b % 2 == 1:
            ans *= a % mod
        a *= a % mod
        b //= 2
    return ans

if k == 1:
    print(1 if n == 1 else 0)
elif n == 1:
    print(k % mod)
elif n == 2:
    print(k * (k - 1) % mod)
else:
    print(k * (k - 1) % mod * f(k - 2, n - 2) % mod)