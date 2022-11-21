n, m = map(int, input().split())
edges = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(lambda e: int(e) - 1, input().split())
    edges[u].add(v)
    edges[v].add(u)
ans = 0
for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            if a in edges[b] and b in edges[c] and c in edges[a]:
                ans += 1
print(ans)