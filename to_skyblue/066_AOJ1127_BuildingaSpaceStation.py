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

while 1:
    n = int(input())
    if n == 0:
        break
    L = tuple(tuple(map(float, input().split())) for _ in range(n))
    dist = []
    for i in range(n):
        x1, y1, z1, r1 = L[i]
        for j in range(i + 1, n):
            x2, y2, z2, r2 = L[j]
            d = (((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
                 - (r1 + r2))
            d = 0 if d < 0 else d
            dist.append((d, i, j))
    dist.sort()
    uf = UnionFind(n)
    ans = 0
    for c, a, b in dist:
        if uf.same(a, b):
            continue
        uf.unite(a, b)
        ans += c
    print(f"{ans:.3f}")