import sys
sys.setrecursionlimit(10**8)

n, q = map(int, input().split())
xl = list(map(int, input().split()))
children = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    children[a].append(b)
    children[b].append(a)
pl = [[] for _ in range(n)]

def dfs(crt, parent):
    p = [xl[crt]]
    for nxt in children[crt]:
        if nxt == parent:
            continue
        dfs(nxt, crt)
        p.extend(pl[nxt])
    pl[crt] = sorted(p, reverse=True)[:20]

dfs(0, -1)

for _ in range(q):
    v, k = map(int, input().split())
    print(pl[v - 1][k - 1])
