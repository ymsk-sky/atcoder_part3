from itertools import product, combinations

n = int(input())
al = [[0] * n for _ in range(n)]
for i in range(n - 1):
    l = list(map(int, input().split()))
    for j in range(n - i - 1):
        al[i][j + i + 1] = l[j]
ans = -float("inf")
for p in product((0, 1, 2), repeat=n):
    gl = [[] for _ in range(3)]
    for i, g in enumerate(p):
        gl[g].append(i)
    tmp = 0
    for g in gl:
        for c in combinations(g, 2):
            tmp += al[c[0]][c[1]]
    ans = max(ans, tmp)
print(ans)
