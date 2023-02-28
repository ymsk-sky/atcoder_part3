"""
1. Bを0 or 1回押す
2. Aを0回以上押す
3. Bを0 or 1回押す
の4通りの内、最小のものが答え
"""
x, y = map(int, input().split())
def f(x, y):
    if x <= y:
        return y - x
    else:
        return float("inf")
print(min(f(x, y), f(x, -y) + 1, f(-x, y) + 1, f(-x, -y) + 2))
