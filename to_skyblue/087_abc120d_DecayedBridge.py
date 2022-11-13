# 必要分だけ実装
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]


"""
M番目, M-1番目, ..., 1番目が落下と,逆順で考える
M->M-1: M番目の橋を復活(unite)する
"""

n, m = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(m)]

uf = UnionFind(n)

ans = [n * (n - 1) // 2]
for i in range(m - 1):
    a, b = abl[m - i - 1]
    a, b = a - 1, b - 1
    if uf.same(a, b):
        # 変化なし(既につながっている)
        ans.append(ans[i])
    else:
        # aとbがつながることで解消される不便度分を前回から減らしていく
        ans.append(ans[i] - (uf.size(a) * uf.size(b)))
    uf.unite(a, b)
print(*ans[::-1], sep="\n")