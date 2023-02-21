k, a, b = map(int, input().split())
if a + 1 >= b:
    print(k + 1)
    exit()
n = k - (a - 1)
if n > 0:
    ans = n//2*(b - a) + a + n%2
    print(ans)
else:
    print(k + 1)
