n = int(input())
al = list(map(int, input().split()))
mod = 998244353

ans = 0
for i in range(1, n + 1):
    # dp[j][k][l]: j番目まででk個選びその和をiで割ったときの余りがlとなる個数
    dp = [[[0] * i for _ in range(i + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for j in range(n):
        a = al[j]
        for k in range(i + 1):
            for l in range(i):
                if k + 1 <= i:
                    l2 = (l + a) % i
                    dp[j + 1][k + 1][l2] += dp[j][k][l]
                    dp[j + 1][k + 1][l2] %= mod
                dp[j + 1][k][l] += dp[j][k][l]
                dp[j + 1][k][l] %= mod
    ans += dp[n][i][0]
    ans %= mod
print(ans)
