from itertools import permutations

n = int(input())
al = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xyl = [list(map(int, input().split())) for _ in range(m)]
xyl = [str(x - 1) + str(y - 1) for x, y in xyl]
INF = float("inf")
ans = INF
s = "".join([str(i) for i in range(n)])
for per in permutations(s):
    line = "".join(per)
    for xy in xyl:
        if xy in line or xy[::-1] in line:
            break
    else:
        tmp = 0
        for i, p in enumerate(per):
            tmp += al[int(p)][i]
        ans = min(ans, tmp)
print(-1 if ans == INF else ans)