n, m, t = map(int, input().split())
al = list(map(int, input().split()))
bl = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    bl[x - 1] = y

for i in range(n - 1):
    t += bl[i]
    if t - al[i] <= 0:
        print("No")
        exit()
    t -= al[i]
print("Yes")