n = int(input())
sl = [list(input()) for _ in range(n)]
for i in range(n - 1, 0, -1):
    for j in range(2, 2*n - 2 + 1):
        if sl[i - 1][j - 1] == "#":
            f = 0
            for p, q in ((1, -1), (1, 0), (1, 1)):
                u, v = i + p, j + q
                if sl[u - 1][v - 1] == "X":
                    f = 1
            if f:
                sl[i - 1][j - 1] = "X"
for l in sl:
    print(*l, sep="")
