import heapq
from collections import deque

n, m, k, s = map(int, input().split())
p, q = map(int, input().split())
danger = [False] * n
for _ in range(k):
    c = int(input())
    danger[c - 1] = True
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)




"""
2<=n<=10**5
1<=m<=2*10**5
0<=k<=n-2
0<=s<=10**5

1<=p<q<=10**5
2<=c<=n-1
1<=a<b<=n
"""
