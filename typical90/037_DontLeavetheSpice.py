"""
037 TLE(5sec)
"""

w, n = map(int, input().split())
lrv = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: i番目まででj[mg]使うときの最大価値
dp = [[0] * (w + 1) for _ in range(n + 1)]
l, r, v = lrv[0]
for j in range(l, r + 1):
    dp[1][j] = v

for i in range(2, n + 1):
    l, r, v = lrv[i - 1]
    ras = [[l, r, 0]]
    bef_v = -1
    st, ed = -1, -1
    for j in range(w + 1):
        dp[i][j] = dp[i - 1][j]  # i番目を作らない場合

        if dp[i - 1][j] > 0 and st == -1 and ed == -1:
            st = j  # 開始地点
        elif dp[i - 1][j] != bef_v and st != -1 and ed == -1:
            ed = j - 1  # 終了地点
            if st + l <= w:
                ras.append([st + l, min(w, ed + r), bef_v])
            st, ed = -1, -1
            if dp[i - 1][j] > 0:
                st = j
        bef_v = dp[i - 1][j]
    if st != -1 and ed == -1:
        if st + l <= w:
            ras.append([st + l, w, bef_v])

    for bl, br, bv in ras:
        for j in range(bl, br + 1):
            # i番目を作る場合
            dp[i][j] = max(dp[i][j], bv + v)

ans = dp[n][w]
print(ans if ans > 0 else -1)