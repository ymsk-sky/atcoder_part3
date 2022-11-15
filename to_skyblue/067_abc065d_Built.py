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
xyl = [list(map(int, input().split())) + [i] for i in range(n)]
edges = []

"""
x軸, y軸で昇順に並べると
最短距離は隣の点となるため
それぞれの軸についてそれらを候補とする
"""
xyl.sort(key=lambda e: e[0])
x1, _, p1 = xyl[0]
for x2, _, p2 in xyl[1:]:
    edges.append((x2 - x1, p1, p2))
    x1, p1 = x2, p2
xyl.sort(key=lambda e: e[1])
_, y1, p1 = xyl[0]
for _, y2, p2 in xyl[1:]:
    edges.append((y2 - y1, p1, p2))
    y1, p1 = y2, p2
edges.sort()

uf = UnionFind(n)

ans = 0
for c, a, b in edges:
    if uf.same(a, b):
        continue
    uf.unite(a, b)
    ans += c
print(ans)