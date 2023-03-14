a, b, c = map(int, input().split())
if b < a < c or c < a < b:
    print("A")
elif a < b < c or c < b < a:
    print("B")
else:
    print("C")
