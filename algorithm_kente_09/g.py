from collections import deque

n, q = map(int, input().split())
l = [[0] * n for _ in range(n)]
ans = []
for _ in range(q):
    m, u, v = map(int, input().split())
    u, v = u - 1, v - 1
    if m == 1:
        l[u][v] = 1 - l[u][v]
        l[v][u] = 1 - l[v][u]
    elif m == 2:
        vis = [0] * n
        vis[u] = 1
        que = deque([u])
        while que:
            crt = que.popleft()
            for nxt in range(n):
                if l[crt][nxt] == 0:
                    continue
                if vis[nxt]:
                    continue
                vis[nxt] = 1
                que.append(nxt)
        if vis[v]:
            ans.append("Yes")
        else:
            ans.append("No")
print(*ans, sep="\n")
