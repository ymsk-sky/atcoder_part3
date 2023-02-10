n, a, b = map(int, input().split())
if (b - a)%2 == 0:
    print((b - a)//2)
else:
    tmp = (a - 1) + 1
    x = tmp + (b - tmp)//2
    tmp = (n - b) + 1
    y = tmp + ((n - a) - tmp)//2
    print(min(x, y))
