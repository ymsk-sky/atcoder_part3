n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b)
    edges[b - 1].append(a)

for edge in edges:
    print(len(edge), *sorted(edge))