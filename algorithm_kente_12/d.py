n, m = map(int, input().split())
edges = [set() for _ in range(n)]
l = [list(map(int, input().split())) for _ in range(m)]
for u, v in l:
    if u > n or v > n or u == v:
        print("No")
        exit()
    u, v = u - 1, v - 1
    if v in edges[u] and u in edges[v]:
        print("No")
        exit()
    edges[u].add(v)
    edges[v].add(u)
print("Yes")
