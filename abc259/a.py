n, m, x, t, d = map(int, input().split())
l = [0] * (n + 1)
l[n] = t
for i in range(n - 1, x - 1, -1):
    l[i] = l[i + 1]
for i in range(x - 1, -1, -1):
    l[i] = l[i + 1] - d
print(l[m])