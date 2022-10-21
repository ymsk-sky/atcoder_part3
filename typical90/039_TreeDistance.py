"""木DP
答えへの貢献度を考える

keyword: 主客転倒
"""
import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
abl = [list(map(int, input().split())) for _ in range(n - 1)]

graph = [[] for _ in range(n + 1)]
for a, b in abl:
    graph[a].append(b)
    graph[b].append(a)

# dp[i]: 頂点iの部下みたいな頂点数
dp = [0] * (n + 1)

def dfs(pos, pre):
    dp[pos] = 1
    for i in graph[pos]:
        if i == pre:
            continue
        dfs(i, pos)
        dp[pos] += dp[i]

dfs(1, 0)

ans = 0
for a, b in abl:
    r = min(dp[a], dp[b])
    ans += r * (n - r)
print(ans)