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

    def size(self, x):
        return -self.root[self.find(x)]

n, m, e = map(int, input().split())
uvl = [list(map(lambda e: int(e) - 1, input().split())) for _ in range(e)]
q = int(input())
xl = [int(input()) - 1 for _ in range(q)]
s = set(xl)
"""
いずれかの発電所に接続されていればよい(区別する必要はない)ため
n~(n+m-1)のm個をすべてnとして扱い, UnionFindのsizeで接続を管理
"""
uf = UnionFind(n + 1)

for i in range(e):
    if i in s:
        continue
    u, v = uvl[i]
    if u > n:
        u = n
    if v > n:
        v = n
    uf.unite(u, v)

ans = [uf.size(n) - 1]
for x in xl[1:][::-1]:
    u, v = uvl[x]
    if u > n:
        u = n
    if v > n:
        v = n
    uf.unite(u, v)
    ans.append(uf.size(n) - 1)
print(*ans[::-1], sep="\n")