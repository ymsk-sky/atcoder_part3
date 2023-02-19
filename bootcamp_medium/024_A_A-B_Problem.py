n, a, b = map(int, input().split())
if a > b:
    print(0)
    exit()
if n == 1:
    if a == b:
        print(1)
    else:
        print(0)
    exit()

min_v = a + b + (n - 2)*a
max_v = a + b + (n - 2)*b
print(max_v - min_v + 1)


"""
4 4 6

4 ? ? 6

4 4 4 6 = 18
4 6 6 6 = 22
"""
