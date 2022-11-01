"""
幅優先探索でトポロジカルソート

dpは「ある状態を処理するとき,その状態に遷移する状態はすべて処理しきっている」必要がある.
よって,dp[i]: 有向パスの最後の頂点がiのときのパスの最長の長さ
と定義しても,頂点の処理順を決める必要がある.

閉路を含まない有向グラフ（=DAG）はパスの処理順を適切に決めることで,
「ある状態を処理するとき,その状態に遷移する状態はすべて処理しきっている」状態を常に満たす順番が存在
-> トポロジカルソートでその順番を見つける

あとはトポロジカルソートした順番にdpを埋めていく
"""
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
into_num = [0] * n  # 項iに入ってくる辺の数
for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    into_num[y - 1] += 1

def topological_sort(into_num):
    q = deque()
    for i in range(n):
        if into_num[i] == 0:
            q.append(i)
    ts = []
    while q:
        v = q.popleft()
        ts.append(v)
        for u in graph[v]:
            into_num[u] -= 1
            if into_num[u] == 0:
                q.append(u)
    return ts

ts = topological_sort(into_num)

dp = [0] * n
for i in range(n):
    u = ts[i]
    for v in graph[u]:
        dp[v] = max(dp[v], dp[u] + 1)

ans = max(dp)
print(ans)