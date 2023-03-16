n, m, q = map(int, input().split())
l = [[] for _ in range(n)]
pl = [n] * m
ans = []
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        i = s[1] - 1
        cnt = 0
        for j in l[i]:
            cnt += pl[j]
        ans.append(cnt)
    else:
        i = s[1] - 1
        j = s[2] - 1
        l[i].append(j)
        pl[j] -= 1

print(*ans, sep="\n")
