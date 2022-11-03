n, m = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for t1 in range(m - 1):
    for t2 in range(t1 + 1, m):
        tmp = 0
        for i in range(n):
            tmp += max(al[i][t1], al[i][t2])
        ans = max(ans, tmp)
print(ans)