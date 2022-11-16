# 045 TLE (ansはAC: これ以上速度アップ見込めず, x5(=40sec)なら間に合うかも)
import sys

def solve():
    input = sys.stdin.readline
    r256 = range(256)
    INF = 10 ** 9
    # sqrt値を事前にメモ
    sql = tuple(tuple((x - y) ** 2 for x in r256) for y in r256)
    ans = []
    while 1:
        n, m = map(int, input().split())
        if n == 0:
            break
        cl = tuple(int(input()) for _ in range(m))

        dp1 = [INF] * 256
        dp2 = [INF] * 256
        dp1[128] = 0
        # yi=y(i-1)+cを境界含めて事前に計算
        decoder = tuple(tuple(255 if i + c > 255 else 0 if i + c < 0 else i + c for c in cl) for i in r256)
        for _ in range(n):
            x = int(input())
            sq = sql[x]
            for yb in r256:
                dpyb = dp1[yb]
                if dpyb == INF:
                    continue
                for y in decoder[yb]:
                    tmp = dpyb + sq[y]
                    if dp2[y] > tmp:
                        dp2[y] = tmp
            dp1 = dp2[:]
            dp2 = [INF] * 256
        ans.append(min(dp1))
    for an in ans:
        print(an)

solve()