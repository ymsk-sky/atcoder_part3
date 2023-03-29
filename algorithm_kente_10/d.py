t, n = map(int, input().split())
ans = [0] * n
for _ in range(t):
    pl = list(map(int, input().split()))
    ans = [max(ans[i], pl[i]) for i in range(n)]
    print(sum(ans))
