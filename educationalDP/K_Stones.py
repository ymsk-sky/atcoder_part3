"""
後退解析(バックトラック)
- 状態の遷移先に負け状態がひとつでもあれば相手を負けにできるので勝ち状態
- 状態の遷移先がすべて勝ちなら負け（るしかない）状態
"""
n, k = map(int, input().split())
al = list(map(int, input().split()))

# dp[i]: 残りi個のときの先手の勝敗(1なら勝ち), 遷移先はn個
dp = [-1] * (k + 1)
for i in range(k + 1):
    cnt = 0
    lose = 0
    for a in al:
        if i - a >= 0:
            cnt += 1
            if dp[i - a] == 0:
                lose += 1
    if cnt == 0:
        dp[i] = 0
    elif lose > 0:
        dp[i] = 1
    else:
        dp[i] = 0
print(["Second", "First"][dp[k]])