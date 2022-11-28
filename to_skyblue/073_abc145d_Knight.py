x, y = map(int, input().split())
mod = 10**9 + 7

M = 2 * 10**6
# f[i]: iの階乗(i!=i*(i-1)*(i-2)*...*3*2*1)
f = [1] * (M + 1)
for i in range(1, M + 1):
    f[i] = f[i - 1] * i % mod

def inv(n):
    """modを法とした逆元
    """
    return pow(n, mod - 2, mod)

# (0,0)->(x,y)への移動に(i+1,j+2)をa回, (i+2,j+1)をb回して移動
# (a+b)C(a) = (a+b)!/(a!*b!)
def calc(x, y):
    a = x
    b = 0
    while a >= 0:
        _x = 1*a + 2*b
        _y = 2*a + 1*b
        if x == _x and y == _y:
            return a, b
        a -= 2
        b += 1
    return 0, 0

a, b = calc(x, y)
if a == 0 and b == 0:
    print(0)
else:
    ans = f[a + b] * inv(f[a]) * inv(f[b]) % mod
    print(ans)