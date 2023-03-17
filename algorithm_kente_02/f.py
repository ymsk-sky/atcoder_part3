import heapq

n = int(input())
d = dict()
for _ in range(n):
    a, b = map(int, input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]

que = []
heapq.heapify(que)

ans = 0
for i in range(1, n + 1):
    if i in d:
        for b in d[i]:
            heapq.heappush(que, -b)
    p = -heapq.heappop(que)
    ans += p
    print(ans)

"""
6
1 8
1 6
2 9
3 1
3 2
4 1

"""
