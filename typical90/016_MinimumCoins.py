n = int(input())
a, b, c = map(int, input().split())
M = 10 ** 4

ans = float("inf")
for i in range(M):
    if a * i > n:
        continue
    for j in range(M):
        if i + j >= M:
            break
        s = n - (a * i + b * j)
        if s < 0:
            break
        if s % c == 0:
            k = s // c
            ans = min(ans, i + j + k)
print(ans)