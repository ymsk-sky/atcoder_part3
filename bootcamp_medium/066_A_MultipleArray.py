n = int(input())
al = []
bl = []
for _ in range(n):
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)

add = 0
for i in range(n - 1, -1, -1):
    a = al[i] + add
    b = bl[i]
    if a%b == 0:
        continue
    cnt = b - a%b
    add += cnt
print(add)
