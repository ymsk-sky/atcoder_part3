from bisect import bisect_left

n = int(input())
al = list(map(int, input().split()))
q = int(input())
bl = [int(input()) for _ in range(q)]

al.sort()

for b in bl:
    ix = bisect_left(al, b)
    if ix == n:
        ans = abs(b - al[ix - 1])
    else:
        ans = min(abs(b - al[ix]), abs(b - al[ix - 1]))
    print(ans)