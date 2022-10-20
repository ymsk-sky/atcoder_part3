"""強連結成分分解(SCC)
- お互いに行き来できる場合同じグループ
- お互いに行き来できない場合違うグループ
グループがk個ありそれぞれa1,a2,...,ak頂点から成る場合
ans = sum([ai * (ai - 1) // 2 for i in range(1, k + 1)])
これは計算量O(N+M)で実現可能

有向グラフにおいて「頂点x,yが互いに到達可能」なことを強連結といい,
どんな有向グラフでも強連結なグループにわけることができる

やり方
1. DFSして帰りがけ順に番号を記録
2. すべての辺の向きを反転させ番号の大きい順にDFS
"""
import sys
sys.setrecursionlimit(10 ** 8)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
hparg = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    hparg[b - 1].append(a - 1)

l = []  # 帰りがけ順の番号記録用
visited = [False] * n

def dfs1(u):
    visited[u] = True
    for v in graph[u]:
        if visited[v]:
            continue
        dfs1(v)
    l.append(u)

cnt = 0
def dfs2(u):
    global cnt
    visited[u] = True
    cnt += 1
    for v in hparg[u]:
        if visited[v]:
            continue
        dfs2(v)

# 1回目のDFS
for i in range(n):
    if visited[i]:
        continue
    dfs1(i)

for i in range(n):
    visited[i] = False
ans = 0
# 2回目のDFS
for i in l[::-1]:
    if visited[i]:
        continue
    cnt = 0
    dfs2(i)
    ans += cnt * (cnt - 1) // 2

print(ans)