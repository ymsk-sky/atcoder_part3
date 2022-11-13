class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        return len(self.roots())


n, m = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(m)]

ans = 0
for i in range(m):
    uf = UnionFind(n)
    for j in range(m):
        if j == i:
            continue
        a, b = abl[j]
        uf.unite(a - 1, b - 1)
    if uf.group_size() > 1:
        ans += 1
print(ans)