import heapq

n = int(input())
al = list(map(int, input().split()))

cnt = 0
for i in range(n):
    a = al[i]
    while a%2 == 0:
        a //= 2
        cnt += 1
    al[i] = a

heapq.heapify(al)
for _ in range(cnt):
    v = heapq.heappop(al)
    v *= 3
    heapq.heappush(al, v)

print(min(al))
