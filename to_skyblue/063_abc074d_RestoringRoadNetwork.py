INF = float("inf")
n = int(input())
al = [list(map(int, input().split())) for _ in range(n)]
bl = [[INF] * n for _ in range(n)]  # 再構築用
for i in range(n):
    bl[i][i] = 0
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        cnt = 0
        for k in range(n):
            if al[i][j] < al[i][k] + al[k][j]:
                cnt += 1
        if cnt == n - 2:
            # i-j間を直接つないでいるのが最短
            ans += al[i][j]
            # 再現
            bl[i][j] = bl[j][i] = al[i][j]
# 再構築
for k in range(n):
    for i in range(n):
        for j in range(n):
            bl[i][j] = min(bl[i][j], bl[i][k] + bl[k][j])
# 確認
for i in range(n):
    for j in range(n):
        if al[i][j] != bl[i][j]:
            print(-1)
            exit()
print(ans)