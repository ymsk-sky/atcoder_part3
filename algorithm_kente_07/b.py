a, b, c = map(int, input().split())
for i in range(a + 1):
    if (a - i) <= b*c:
        print((a - i)/b)
        break
