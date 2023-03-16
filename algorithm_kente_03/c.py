a, r, n = map(int, input().split())

if r == 1:
    print(a)
elif n > 30:
    print("large")
else:
    v = a*r**(n - 1)
    print("large" if v > 10**9 else v)
