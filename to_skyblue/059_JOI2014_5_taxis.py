"""
メモリ
-> crlをtupleに変更
速度
-> solve()関数で処理
-> sys.stdinで入力受付
-> 値を使わないfor文はrange(N)ではなく[0]*Nで回す
"""

import heapq
from collections import deque
from sys import stdin

def solve():
    n, k = map(int, stdin.readline().split())
    crl = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    edges = [[] for _ in range(n)]
    for _ in [0] * k:
        a, b = map(int, stdin.readline().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)

    INF = float("inf")

    able = [[] for _ in range(n)]
    # 事前に各町からタクシーで移動可能な町をリストアップ
    for i in range(n):
        dist = [INF] * n
        dist[i] = 0
        q = deque()
        q.append(i)
        while q:
            crt = q.popleft()
            for nxt in edges[crt]:
                if dist[nxt] != INF:
                    continue
                dist[nxt] = dist[crt] + 1
                if dist[nxt] < crl[i][1]:
                    q.append(nxt)
        able[i] = [j for j in range(n) if 1 < dist[j] <= crl[i][1]]

    dist = [INF] * n
    dist[0] = 0
    que = []
    heapq.heapify(que)
    heapq.heappush(que, (0, 0))
    
    while que:
        d, crt = heapq.heappop(que)
        if d > dist[crt]:
            continue
        for nxt in edges[crt] + able[crt]:
            tmp = crl[crt][0] + dist[crt]
            if tmp < dist[nxt]:
                dist[nxt] = tmp
                heapq.heappush(que, (tmp, nxt))

    print(dist[n - 1])

solve()