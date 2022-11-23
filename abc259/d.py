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
sx, sy, tx, ty = map(int, input().split())
circles = [list(map(int, input().split())) for _ in range(n)]

uf = UnionFind(n + 2)

for i in range(n):
    x1, y1, r1 = circles[i]
    # スタート地点と接するか
    d = ((x1 - sx)**2 + (y1 - sy)**2)
    if d == r1**2:
        uf.unite(i, n)
    # ゴール地点と接するか
    d = ((x1 - tx)**2 + (y1 - ty)**2)
    if d == r1**2:
        uf.unite(i, n + 1)
    # ほかの円と接するか
    for j in range(i + 1, n):
        x2, y2, r2 = circles[j]
        d = ((x2 - x1)**2 + (y2 - y1)**2)
        if d > (r1 + r2)**2 or d < (r2 - r1)**2:
            continue
        uf.unite(i, j)

if uf.same(n, n + 1):
    print("Yes")
else:
    print("No")