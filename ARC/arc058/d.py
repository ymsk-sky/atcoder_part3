h, w, a, b = map(int, input().split())
mod = 10**9 + 7
M = 2 * 10**5
fl = [1] * (M + 1)  # fl[i]: i!
for i in range(1, M + 1):
    fl[i] = fl[i - 1] * i % mod
def inv(n):
    return pow(n, mod - 2, mod)
"""
s->(1->2)->t
s......
.......
....111
####222
####...
####..t
"""
l1 = [] # 1
for j in range(b, w):  # 右にj回移動
    c = fl[h - 1 - a + j] * inv(fl[j]) * inv(fl[h - 1 - a]) % mod
    l1.append(c)
ans = 0
for j in range(len(l1)):
    ans += l1[j] * fl[a - 1 + w - 1 - b - j] * inv(fl[a - 1]) * inv(fl[w - 1 - b - j]) % mod
    ans %= mod
print(ans)