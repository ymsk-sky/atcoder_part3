"""
(1,1)->(h,w)への移動方法

移動は((h-1)+(w-1))=(h+w-2)回で「下移動」と「右移動」の組み合わせとなるため,
(h+w-2)C(h-1) or (h+w-2)C(w-1)

-> (h+w-2)回の試行の内,(h-1)回をどこで行うか
-> (h+w-2)個から(h-1)個を入れる位置を選択 と考える

実際の計算は (h+w-2)!/(h-1)!(w-1)!

またフェルマーの小定理により
pを素数とすると a**(p-1)=1(mod p) が成立
両辺にa**(-1)をかけて a**(p-2)=a**(-1)(mod p)
a**(-1)はつまりaで割ることと同じなのでpを法とするならば, aで割る=>a**(p-2)をかけることと同じになる

references:
    https://kakedashi-engineer.appspot.com/2020/05/01/abc034c/
    https://kusozakokyopro.wordpress.com/2019/05/16/atcoder-abc034-c-%E7%B5%8C%E8%B7%AF/
"""
h, w = map(int, input().split())
mod = 10**9 + 7

M = 2 * 10**5  # h,w<=10**5のため
# f[i]: iの階乗(i!=i*(i-1)*(i-2)*...*3*2*1)
f = [1] * (M + 1)
for i in range(1, M + 1):
    f[i] = f[i - 1] * i % mod

def inv(n):
    """modを法とした逆元
    """
    return pow(n, mod - 2, mod)

# (h+w-2)!/(h-1)!(w-1)! = (h+w-2)*inv(h-1)*(w-1)
ans = f[h + w - 2] * inv(f[h - 1]) * inv(f[w - 1]) % mod
print(ans)