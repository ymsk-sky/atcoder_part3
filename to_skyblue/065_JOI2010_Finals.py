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


n, m, k = map(int, input().split())
edges = []
for _ in [0] * m:
    a, b, c = map(int, input().split())
    edges.append((c, a - 1, b - 1))
edges.sort()

uf = UnionFind(n)

ans = 0
l = n
for c, a, b in edges:
    if l == k:
        break

    if uf.same(a, b):
        continue
    l -= 1
    uf.unite(a, b)
    ans += c

print(ans)