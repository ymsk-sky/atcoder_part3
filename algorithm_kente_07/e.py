n = int(input())
for k in range(1, 31):
    x = 1
    for i in range(1, 31):
        x *= 3
        if i == k:
            x += 1
    if x == n:
        print(k)
        break
else:
    print(-1)
