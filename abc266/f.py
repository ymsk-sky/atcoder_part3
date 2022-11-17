"""
N頂点N辺の連結な単純無向グラフ
-> 閉路がただ一つ存在
単純グラフ:
    - 自己ループなし
    - 多重辺をもたない

閉路を見つけ, 閉路上の頂点は単純パスが一意ではない
"""

from collections import deque

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

n = int(input())
edges = [[] for _ in range(n)]
into = [0] * n  # 入次数
for _ in range(n):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)
    into[u] += 1
    into[v] += 1

# 閉路検出: 入次数が1の頂点を消していき残った頂点が閉路
cycle = [len(edge) != 1 for edge in edges]  # 入次数が1の場合,葉(閉路でない)確定
que = deque()
for i in range(n):
    if len(edges[i]) == 1:
        que.append(i)
while que:
    crt = que.popleft()
    for nxt in edges[crt]:
        if not cycle[nxt]:
            # 閉路でないことが確定している場合
            continue
        # 次数を減らす
        into[nxt] -= 1
        # 次数が1以下になった場合閉路ではないことが確定
        if into[nxt] <= 1:
            cycle[nxt] = False
            que.append(nxt)

# 部分木作成: union-findで実装, x,yが同じ部分木に含まれる場合パスは一意
# (x,yが違う部分木に含まれる場合は, 閉路を通ることで一意とならないため)
uf = UnionFind(n)
# BFSで閉路上の頂点を根とする部分木をそれぞれUnionFindで連結していく
visited = [False] * n
for i in range(n):
    if not cycle[i]:
        continue
    que = deque([i])
    visited[i] = True
    while que:
        crt = que.popleft()
        for nxt in edges[crt]:
            if visited[nxt] or cycle[nxt]:
                continue
            visited[nxt] = True
            que.append(nxt)
            uf.unite(crt, nxt)

q = int(input())
ans = []
for _ in range(q):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    if uf.same(x, y):
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans, sep="\n")