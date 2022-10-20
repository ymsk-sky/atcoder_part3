"""二部グラフ
辺で直接結ばれた頂点同士が互いに違う色になるように,
頂点を2色で塗ることができるグラフ

性質
- 奇数長の閉路を含まない
- 最大マッチングが多項式時間で計算できる

"" 木は必ず二部グラフ ""
->木を2彩色したとき,少なくとも片方は2/N個以上の頂点をもつので,
回答は,頂点数の多い方の色で塗られた頂点から2/N個選んで出力すればよい

2彩色はDFSで実装可能
"""
import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# 2彩色 兼 visited(-1=False, 0or1=True)
col = [-1] * n
# u: position, c: color
def dfs(u, c):
    col[u] = c
    for v in graph[u]:
        if col[v] == -1:
            # c=1: 1-c=0, c=0: 1-c=1
            dfs(v, 1 - c)
dfs(1, 1)

ans = []
i = 0
cnt = 0
n2 = n // 2
val = 0 if col.count(1) < n2 else 1
while cnt < n2:
    if col[i] == val:
        ans.append(i + 1)
        cnt += 1
    i += 1
print(*ans)