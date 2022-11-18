n, p, q, r = map(int, input().split())
al = list(map(int, input().split()))
acc = [0] * (n + 1)
for i in range(n):
    acc[i + 1] = acc[i] + al[i]

y = z = w = 0
for x in range(n):
    while acc[y] - acc[x] < p and y < n:
        y += 1
    if acc[y] - acc[x] == p:
        while acc[z] - acc[y] < q and z < n:
            z += 1
        if acc[z] - acc[y] == q:
            while acc[w] - acc[z] < r and w < n:
                w += 1
            if acc[w] - acc[z] == r:
                print("Yes")
                exit()
print("No")