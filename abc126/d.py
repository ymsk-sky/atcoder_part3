"""
DFS(深さ優先探索)
シンプルに距離が偶数のとき同じ色,奇数のとき違う色にする

「木」なのでループしない
-> ansの値の確認は必要なく,ある位置から行ける位置に移動し続ければいずれ完了する
"""

import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    w %= 2
    graph[u].append([v, w])
    graph[v].append([u, w])

ans = [-1] * n

def dfs(u, pa=-1, col=0):
    """
    u: 現在地
    pa: ひとつ前の位置
    col: 現在の色
    """
    ans[u] = col
    for v, w in graph[u]:
        if v == pa:
            # 逆走しない
            continue
        if w % 2 == 0:
            # u-vの距離が偶数: 同じ色
            dfs(v, u, col)
        else:
            # u-vの距離が奇数: 色を反転
            dfs(v, u, 1 - col)
dfs(0)
print(*ans, sep="\n")