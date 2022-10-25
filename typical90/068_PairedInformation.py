import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
q = int(input())
l = [list(map(int, input().split())) for _ in range(q)]

d = dict()
for i in range(1, n + 1):
    d[i] = dict()

visited = [-1] * (n + 1)

def search(x, y, v, bef, i):
    visited[x] = i
    if y in d[x]:
        return d[x][y] - v
    else:
        for k in d[x]:
            if k == bef or visited[k] == i:
                continue
            s = search(k, y, d[x][k] - v, x, i)
            if type(s) != str:
                return s
    return "Ambiguous"

for i in range(q):
    t, x, y, v = l[i]
    if t == 0:
        # al[x] + al[y](=al[x+1]) = v
        d[x][y] = v
        d[y][x] = v
    elif t == 1:
        # al[x]=vとしたらal[y]は何か出力
        ans = search(x, y, v, -1, i)
        print(ans)