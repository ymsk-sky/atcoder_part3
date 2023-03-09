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


n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n + m)]

dist = [[0] * (n + m) for _ in range(n + m)]
for i in range(n + m):
    ax, ay, ac = l[i]
    for j in range(i + 1, n + m):
        bx, by, bc = l[j]
        d = ((ax - bx)**2 + (ay - by)**2)**0.5
        if ac != bc:
            d *= 10
        dist[i][j] = dist[j][i] = d

ans = float("inf")
for s in range(1<<m):
    # s集合の小さい塔を含ませる
    kl = [n + k for k in range(m) if (s>>k)&1] + list(range(n))
    el = []
    for i in kl:
        for j in kl:
            if i == j:
                continue
            el.append((dist[i][j], i, j))
    el.sort()
    uf = UnionFind(n + m)
    tmp = 0
    for cost, u, v in el:
        if uf.same(u, v):
            continue
        uf.unite(u, v)
        tmp += cost
    ans = min(ans, tmp)
print(ans)
