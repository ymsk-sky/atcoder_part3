import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n):
    u, k, *l = map(int, input().split())
    edges[u - 1] = l

dl = [0] * n
fl = [0] * n

t = 1
def dfs(crt):
    global t
    dl[crt - 1] = t
    for nxt in edges[crt - 1]:
        if dl[nxt - 1] > 0:
            continue
        t += 1
        dfs(nxt)
    t += 1
    fl[crt - 1] = t

for i in range(1, n + 1):
    if dl[i - 1] == 0:
        dfs(i)
        t += 1

for i in range(n):
    print(i + 1, dl[i], fl[i])