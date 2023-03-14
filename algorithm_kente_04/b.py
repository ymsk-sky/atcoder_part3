x, y = map(int, input().split())
if y == 0:
    print("ERROR")
    exit()
ans = int(100*x/y)
print(f"{ans/100:.2f}")
