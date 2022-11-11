from bisect import bisect_right, bisect_left

n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))

al.sort()
cl.sort()

ans = 0
for b in bl:
    i = bisect_left(al, b)
    j = n - bisect_right(cl, b)
    ans += i * j
print(ans)