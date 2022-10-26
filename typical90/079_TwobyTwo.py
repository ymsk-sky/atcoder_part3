h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]
bl = [list(map(int, input().split())) for _ in range(h)]

dl = [[bl[i][j] - al[i][j] for j in range(w)] for i in range(h)]
cnt = 0
for i in range(h - 1):
    for j in range(w - 1):
        v = -dl[i][j]
        dl[i][j] += v
        dl[i + 1][j] += v
        dl[i][j + 1] += v
        dl[i + 1][j + 1] += v
        cnt += abs(v)

for i in range(h):
    if sum(dl[i]) == 0:
        continue
    else:
        print("No")
        exit()
print("Yes")
print(cnt)