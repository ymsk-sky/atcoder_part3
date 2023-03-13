import sys
sys.setrecursionlimit(10**7)

n, x = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append((c, b))
    edges[b].append((c, a))

def dfs(crt, bef, cost):
    if cost == x:
        print("Yes")
        exit()
    for nxt_cost, nxt in edges[crt]:
        if nxt == bef or cost + nxt_cost > x:
            continue
        dfs(nxt, crt, cost + nxt_cost)

for i in range(n):
    dfs(i, -1, 0)

print("No")
