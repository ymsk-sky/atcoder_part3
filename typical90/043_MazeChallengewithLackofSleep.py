"""
拡張BFS
dist[i][j][0]: (i,j)で上を向くまでの最小回数
dist[i][j][1]: (i,j)で右を向くまでの最小回数
dist[i][j][2]: (i,j)で下を向くまでの最小回数
dist[i][j][3]: (i,j)で左を向くまでの最小回数
を更新していく
01-BFSは計算量O(HW)
"""
from collections import deque

def solve():
    h, w = map(int, input().split())
    rs, cs = map(lambda x: int(x) - 1, input().split())
    rt, ct = map(lambda x: int(x) - 1, input().split())
    maze = [input() for _ in range(h)]

    INF = float("inf")
    dist = [[[INF] * 4 for _ in range(w)] for _ in range(h)]
    q = deque()
    for i in range(4):
        dist[rs][cs][i] = 0
        q.append((rs, cs, i))
    """
      0
    3 p 1
      2
    """
    o = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        r, c, d = q.popleft()
        for way in range(4):
            i, j = r + o[way][0], c + o[way][1]
            if 0 <= i < h and 0 <= j < w:
                if maze[i][j] == "#":
                    continue
                if d == way:
                    if dist[i][j][way] > dist[r][c][d]:
                        dist[i][j][way] = dist[r][c][d]
                        q.appendleft((i, j, way))
                elif (d - way) % 2 == 1:
                    if dist[i][j][way] > dist[r][c][d] + 1:
                        dist[i][j][way] = dist[r][c][d] + 1
                        q.append((i, j, way))

    print(min(dist[rt][ct]))

solve()