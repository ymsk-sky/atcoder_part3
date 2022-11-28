"""
1<=a1<a2<...<ak<=n
を考えてみる. これは1以上n以下の整数から異なるk個を選んで並び変えれば満たせるため
n個からk個を選ぶ組み合わせに等しく nCk となる.

1<=a1<=a2<=...<=ak<=n
の場合は, 重複を許して1以上n以下の整数からk個を選んで並び替えることで満たせる.
よって (n+k-1)Ck となる.
-> (n+k-1)!/(k!(n-1)!)
"""
n = int(input())
k = int(input())
mod = 10**9 + 7

M = 2 * 10**5
# f[i]: iの階乗(i!=i*(i-1)*(i-2)*...*3*2*1)
f = [1] * (M + 1)
for i in range(1, M + 1):
    f[i] = f[i - 1] * i % mod

def inv(n):
    """modを法とした逆元
    """
    return pow(n, mod - 2, mod)

ans = f[n + k - 1] * inv(f[k]) * inv(f[n - 1]) % mod
print(ans)