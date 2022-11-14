import sys

def solve():
    INF = 10 ** 8
    M = 10 ** 6

    dp = [INF] * (M + 1)
    dp_odd = [INF] * (M + 1)
    dp[0] = 0
    dp_odd[0] = 0

    for i in range(1, 10 ** 3):
        a = i * (i + 1) * (i + 2) // 6
        if a > M:
            break
        if a & 1 == 1:
            for n in range(M - a):
                cost = dp[n] + 1
                if dp[n + a] > cost:
                    dp[n + a] = cost
                cost_odd = dp_odd[n] + 1
                if dp_odd[n + a] > cost_odd:
                    dp_odd[n + a] = cost_odd
        else:
            for n in range(M - a):
                cost = dp[n] + 1
                if dp[n + a] > cost:
                    dp[n + a] = cost

    ans = []
    while 1:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        ans.append((dp[n], dp_odd[n]))

    for an in ans:
        print(*an)

solve()