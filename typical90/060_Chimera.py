from bisect import bisect_left

n = int(input())
al = list(map(int, input().split()))

l = [0] * n
r = [0] * n

lax = []
rax = []
for k in range(n):
    a = al[k]
    b = al[n - 1 - k]

    il = bisect_left(lax, a)
    if il == len(lax):
        lax.append(a)
    else:
        lax[il] = a
    l[k] = il + 1

    ir = bisect_left(rax, b)
    if ir == len(rax):
        rax.append(b)
    else:
        rax[ir] = b
    r[n - 1 - k] = ir + 1

ans = 0
for k in range(n):
    tmp = l[k] + r[k] - 1
    ans = max(ans, tmp)
print(ans)