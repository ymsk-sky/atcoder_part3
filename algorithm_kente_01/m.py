"""二分探索
あるstrong以上になるかを二分探索するときa,b,c,d,eを選ぶとすると
(B[a]+B[b]+B[c]+B[d]+B[e])/(A[a]+A[b]+A[c]+A[d]+A[e]) >= strong
B[a]+B[b]+B[c]+B[d]+B[e] >= strong*(A[a]+A[b]+A[c]+A[d]+A[e])
B[a]+B[b]+B[c]+B[d]+B[e] - strong*(A[a]+A[b]+A[c]+A[d]+A[e]) >= 0
strong => s
(B[a]-sA[a]) + (B[b]-sA[b]) + (B[c]-sA[c]) + (B[d]-sA[d]) + (B[e]-sA[e]) >= 0
となるのでB[i]-sA[i]が大きい5つを選択すればよい
"""
n, m = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(n)]
cdl = [list(map(int, input().split())) for _ in range(m)]

def check(s):
    xl = [abl[i][1] - s*abl[i][0] for i in range(n)]
    yl = [cdl[i][1] - s*cdl[i][0] for i in range(m)]
    xl.sort(reverse=True)
    yl.sort(reverse=True)

    # 普通のモンスターのみ
    res = sum(xl[:5])
    if res >= 0:
        return True
    # お助けモンスターを使用
    res -= xl[4]
    res += yl[0]
    return res >= 0

left = 0
right = 10**6
for _ in range(10**4):
    mid = (left + right) / 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
