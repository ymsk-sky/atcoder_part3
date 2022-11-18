h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]

for h in range(1 << h1):
    if bin(h).count("1") != h2:
        continue
    for w in range(1 << w1):
        if bin(w).count("1") != w2:
            continue
        c = []
        for i in range(h1):
            if (h >> i) & 1:
                l = [a[i][j] for j in range(w1) if (w >> j) & 1]
                c.append(l)
        if c == b:
            print("Yes")
            exit()
print("No")