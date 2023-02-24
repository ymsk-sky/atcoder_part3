n, k, s = map(int, input().split())
M = 10**9
if s == M:
    if k == 0:
        ans = [M - 1] * n
    else:
        ans = [M] * k
        for _ in range(n - k):
            ans.append(1)
else:
    if k == 0:
        ans = [M] * n
    else:
        ans = [s] * k
        for _ in range(n - k):
            ans.append(M)

print(*ans)
