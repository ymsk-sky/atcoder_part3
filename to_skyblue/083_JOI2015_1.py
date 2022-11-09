n, m = map(int, input().split())
pl = list(map(int, input().split()))
abcl = [list(map(int, input().split())) for _ in range(n - 1)]

# num[i]: iから(i+1)の間を通る回数 [x-1, 1-2, 2-3, 3-4, 4-x]
num = [0] * (n + 1)
for p, q in zip(pl, pl[1:]):
    if p > q:
        p, q = q, p
    num[p] += 1
    num[q] -= 1
for i in range(n):
    num[i + 1] += num[i]

ans = 0
for i in range(1, n):
    a, b, c = abcl[i - 1]
    k = num[i]
    ans += min(a * k, b * k + c)
print(ans)