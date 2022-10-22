"""
半分全挙列
2**N通りをすべて調べるのは不可能
->ふたつのグループにわけてからそれぞれ全挙列し組み合わせる
各グループの全挙列は個数が半分になっているのでO(N*2**(N/2))で間に合う

各グループでいくつか選んだ時の値段をリスト所持し,
グループ1 + グループ2 で合わせてK個になるような組み合わせを探索

その際の探索は, 上限の境目がわかれば個数は判明するのでリストを昇順で所持し二分探索
"""
from bisect import bisect_right
from itertools import combinations

n, k, p = map(int, input().split())
al = list(map(int, input().split()))

# alを2グループにわける
xl = []
yl = []
for i in range(n):
    if i % 2 == 0:
        xl.append(al[i])
    else:
        yl.append(al[i])

# i個の組み合わせのときの合計値一覧
axl = [[0]]
ayl = [[0]]
for i in range(1, k + 1):
    x = []
    if len(xl) >= i:
        for comb in combinations(xl, i):
            x.append(sum(comb))
    axl.append(x)
    y = []
    if len(yl) >= i:
        for comb in combinations(yl, i):
            y.append(sum(comb))
    ayl.append(y)

# 各合計値リストを昇順にする
for i in range(len(axl)):
    axl[i] = sorted(axl[i])
for i in range(len(ayl)):
    ayl[i] = sorted(ayl[i])

ans = 0
# 合わせてk個になるような組み合わせを探索(それぞれ0~k,k~0個)
for i in range(k + 1):
    j = k - i
    if i > len(axl) - 1 or j > len(ayl) - 1:
        continue
    for ax in axl[i]:
        idx = bisect_right(ayl[j], p - ax)
        ans += idx
print(ans)