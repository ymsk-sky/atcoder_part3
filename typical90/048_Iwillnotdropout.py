import heapq

def solve():
    n, k = map(int, input().split())
    l = []
    for _ in range(n):
        a, b = map(int, input().split())
        l.append((-b, -a))
    heapq.heapify(l)

    ans = 0
    for _ in range(k):
        val, nxt = heapq.heappop(l)
        ans -= val
        if nxt < 0:
            heapq.heappush(l, (nxt - val, -val))
    print(ans)

solve()