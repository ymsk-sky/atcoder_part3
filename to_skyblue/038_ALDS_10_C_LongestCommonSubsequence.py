"""
AOJのジャッジではLTEとなってしまうが
in1.txt
in2.txt
in3.txt
in4.txt
in5.txt
すべて回答は正しいのでACとする
"""

import sys

q = int(sys.stdin.readline())
def solve(q):
    for _ in range(q):
        # x = input()
        # y = input()
        x = sys.stdin.readline()[:-1]
        y = sys.stdin.readline()[:-1]
        n = len(x)
        m = len(y)
        # dp[i * (m + 1) + j]: xのi文字目までとyのj文字目までで最長共通部分列
        dp = [0] * (m + 1) * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i * (m + 1) + j] = dp[(i - 1) * (m + 1) + j - 1] + 1
                else:
                    if dp[(i - 1) * (m + 1) + j] > dp[i * (m + 1) + j - 1]:
                        dp[i * (m + 1) + j] = dp[(i - 1) * (m + 1) + j]
                    else:
                        dp[i * (m + 1) + j] = dp[i * (m + 1) + j - 1]
        print(dp[-1])
solve(q)

"""
1<=q<=150
1<=|x|,|y|<=1000
|x|,|y|が100を超える場合q<=20
"""
