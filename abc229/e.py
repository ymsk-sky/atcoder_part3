from collections import defaultdict

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

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        return len(self.roots())

    def group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n + 1):
            group_members[self.find(member)].append(member)
        return group_members


n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)

uf = UnionFind(n)

cnt = 0
ans = [cnt]
for i in range(n - 1, 0, -1):
    tmp = 0
    for j in edges[i]:
        if j < i:
            continue
        if not uf.same(i, j):
            tmp += 1
        uf.unite(i, j)
    # 最初の連結はカウントは変化なし, それ以降は違う塊同士が接続されることになる
    cnt -= max(0, tmp - 1)
    if uf.size(i) == 1:
        cnt += 1
    ans.append(cnt)

print(*ans[::-1], sep="\n")