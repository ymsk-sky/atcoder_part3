n, m, q = map(int, input().split())
# cnt[L][R]: L発R着
cnt = [[0] * (n + 1) for _ in range(n + 1)]
for _ in [0] * m:
    l, r = map(int, input().split())
    cnt[l][r] += 1
# cnt[L][R]: 累積和 区間[L,1],[L,2],...,[L,R]の列車の台数
for i in range(1, n + 1):
    for j in range(1, n + 1):
        cnt[i][j] += cnt[i][j - 1]

ans = []
for _ in [0] * q:
    p, q = map(int, input().split())
    tmp = 0
    # p~q発でq着の列車
    for i in range(p, q + 1):
        tmp += cnt[i][q]
    ans.append(tmp)

print(*ans, sep="\n")