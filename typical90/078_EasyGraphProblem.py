n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

ans = 0
for i in range(n):
    cnt = 0
    for j in graph[i]:
        if j < i:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)