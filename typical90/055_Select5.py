from itertools import combinations

n, p, q = map(int, input().split())
al = list(map(int, input().split()))

l = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        v = al[i] * al[j] % p
        l[i][j] = v
        l[j][i] = v

ans = 0
for c in combinations(range(n), 5):
    s = l[c[0]][c[1]]
    s *= l[c[2]][c[3]]
    s %= p
    s *= al[c[4]]
    if s % p == q:
        ans += 1
print(ans)