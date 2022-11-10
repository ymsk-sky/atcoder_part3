import sys
sys.setrecursionlimit(10 ** 8)

n, q = map(int, input().split())

edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)

cnt = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    cnt[p - 1] += x

# DFS
def dfs(crt, bef):
    for nxt in edges[crt]:
        if nxt == bef:
            continue
        cnt[nxt] += cnt[crt]
        dfs(nxt, crt)

dfs(0, -1)

print(*cnt)