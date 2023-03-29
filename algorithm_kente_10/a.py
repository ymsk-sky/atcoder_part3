a, b, c = map(int, input().split())
a, b, c = a*b, a*c, b*c
print(min(a, b, c), max(a, b, c))
