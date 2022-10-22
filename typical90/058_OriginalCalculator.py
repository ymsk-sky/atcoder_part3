n, k = map(int, input().split())
if n == 0:
    print(0)
    exit()

mod = 10 ** 5

# l[i]=v: 値がiになるときのボタンを押した回数v
l = [-1] * mod

x = n
i = 0
while 1:
    i += 1  # ボタン押す
    y = sum([(x // 10 ** i) % 10 for i in range(5)])  # y計算
    z = (x + y) % mod  # z計算
    x = z  # x更新
    if l[x] > 0:
        break
    l[x] = i

pre = [-1] * l[x]  # ループ前に(l[x] - 1)個 + 1個(0用)
loop = [-1] * ((i - 1) - l[x] + 1)  # l[x] ~ (i-1) までがループする
for j in range(mod):
    if l[j] == -1:
        continue
    if l[j] < l[x]:
        pre[l[j]] = j
    else:
        loop[l[j] - l[x]] = j
"""99999 1000000000000000000
1, 2,..., 48,  49,   50, ..., 4783,
             4784, 4785, ...,
     pre     loooooooooooooooooooop
"""

if k < l[x]:
    print(pre[k])
else:
    k -= l[x]
    print(loop[k % len(loop)])

"""
0<=n<=99999=10**5-1
1<=k<=10**18

x表示時
1. xの各桁の和をyとする
2. z = (x + y) % mod ->0<=z<=99999
3. x = z

n表示時にk回押す

y = sum([(x // 10 ** i) % 10 for i in range(5)])
z = (x + y) % mod
x = z

99999 1000000000000000000
84563

pre + loop (preが0の可能性もある)
0 1 2 3 4 5 6 7 8 9
n 2 4 8 3 1 8 3 1 8
  pre looooooooooop
"""
