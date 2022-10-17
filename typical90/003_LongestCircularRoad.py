"""
「どの都市の間も、いくつかの道路を通って移動可能なもの」より,
"N頂点, (N-1)辺の連結なグラフ(木構造)" を考える.

木構造の特徴:
- 頂点uからvへの単純パスはただ一つ
- u,vを結ぶ辺をひとつ追加するとき閉路はただ一つとなり, その長さは(u->vの長さ)+1となる

よって, 単純パスの長さの最大値(=最短距離の最大値)Eを求めればよい(E+1が答え)
このEを木の直径という

木の直径は
1. 頂点1から最短距離を求める: O(N)
2. 最短距離が最大の頂点uを求める: O(N)
3. 頂点uから再度, 最短距離を求める: O(N)
4. 2.で出現した最大距離がEの値
-> O(N)で回答可能
"""
from collections import deque

n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

INF = float("inf")

# stから最大の都市とその距離を返すBFS
def bfs(st):
    dist = [INF] * (n + 1)
    dist[st] = 0
    q = deque([st])
    while q:
        pos = q.popleft()
        for nxt in edges[pos]:
            if dist[nxt] != INF:
                continue
            dist[nxt] = dist[pos] + 1
            q.append(nxt)
    d, u = max([[dist[i], i] for i in range(1, n + 1)])
    return u, d

# 1回目: 1からの最短経路が最大の都市uを求める
u, _ = bfs(1)
# 2回目: uからの最短経路が最大の距離eを求める
_, e = bfs(u)
# E+1が木の直径
print(e + 1)