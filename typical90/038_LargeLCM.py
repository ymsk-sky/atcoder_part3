from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)
a, b = map(int, input().split())
ans = lcm(a, b)
if ans > 10 ** 18:
    print("Large")
else:
    print(ans)