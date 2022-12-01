from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
s, t = map(int, input().split())
s, t = s - 1, t - 1
# 1,2,3回目で既に訪れたか
visited = [[-1] * 3 for _ in range(n)]
visited[s][2] = 0

que = deque()
que.append((s, 2))
while que:
    crt, num = que.popleft()
    for nxt in graph[crt]:
        if visited[nxt][(num + 1) % 3] < 0:
            x = 0 if num < 2 else 1
            visited[nxt][(num + 1) % 3] = visited[crt][num] + x
            que.append((nxt, (num + 1) % 3))
print(visited[t][2])