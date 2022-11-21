y = int(input())
for i in range(2000, 3003):
    if i >= y and i % 4 == 2:
        print(i)
        break