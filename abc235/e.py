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


n, m, q = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a - 1, b - 1, -1))
for i in range(q):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1, i))

edges.sort()
ans = [-1] * q
uf = UnionFind(n)
for _, a, b, x in edges:
    if uf.same(a, b):
        if x >= 0:
            ans[x] = 0
        continue
    if x >= 0:
        ans[x] = 1
    else:
        uf.unite(a, b)

for x in ans:
    print("Yes" if x == 1 else "No")