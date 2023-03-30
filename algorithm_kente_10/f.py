h, w, n = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]
cl = list(map(int, input().split()))
for i in range(h):
    for j in range(w):
        a = al[i][j]
        for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            u, v = i + p, j + q
            if 0 > u or u >= h or 0 > v or v >= w:
                continue
            b = al[u][v]
            if a == b:
                continue
            if cl[a - 1] == cl[b - 1]:
                print("No")
                exit()
print("Yes")
