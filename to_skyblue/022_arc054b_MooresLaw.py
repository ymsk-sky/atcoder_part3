import math

p = float(input())

def f(x):
    return x + p/(2**(x/1.5))

def fd(x):
    # f'(x)
    return 1 + p*(2**(-x/1.5))*math.log(2**(-1/1.5))

left = 0
right = p
for _ in [0] * 1000:
    mid = (left + right) / 2
    tmp = fd(mid)
    if tmp == 0:
        break
    elif tmp < 0:
        left = mid
    else:
        right = mid
print(f"{f(mid)}")
