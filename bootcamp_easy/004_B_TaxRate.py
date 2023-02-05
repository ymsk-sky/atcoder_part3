n = int(input())
x1 = int(n / 1.08)
x2 = int(-(-n // 1.08))
if int(x1 * 1.08) == n:
    print(x1)
elif int(x2 * 1.08) == n:
    print(x2)
else:
    print(":(")