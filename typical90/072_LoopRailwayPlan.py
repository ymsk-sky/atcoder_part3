h, w = map(int, input().split())
c = [input() for _ in range(h)]

graph = [[] for _ in range(h * w)]
for i in range(h):
    for j in range(w):
        if c[i][j] == "#":
            continue
        n = j + i * w
        for u, v in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            if 0 <= i + u < h and 0 <= j + v < w:
                if c[i + u][j + v] == "#":
                    continue
                m = (j + v) + (i + u) * w
                graph[n].append(m)

ans = 0
def dfs(st, crt, visited):
    global ans
    for nxt in graph[crt]:
        if nxt == st:
            ans = max(ans, visited.count(True))
        elif visited[nxt]:
            continue
        else:
            visited[nxt] = True
            dfs(st, nxt, visited)
            visited[nxt] = False

for n in range(h * w):
    if c[n // w][n % w] == "#":  # n = j + i * w
        continue
    visited = [False] * (h * w)
    visited[n] = True
    dfs(n, n, visited)

print(ans if ans > 2 else -1)