a, b, c = map(int, input().split())
left = 1
right = 2
for _ in range(10**4):
    x = (left + right)/2
    v = a*x**5 + b*x + c
    if v == 0:
        left = x
        break
    elif v < 0:
        left = x
    else:
        right = x
print(left)
