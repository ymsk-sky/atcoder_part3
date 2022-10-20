"""
素因数列挙の計算量はO(NloglogN)

keyword: エラトステネスの篩
"""

n, k = map(int, input().split())

c = [0] * (n + 1)
for i in range(2, n + 1):
    if c[i] >= 1:
        continue
    for j in range(i, n + 1, i):
        c[j] += 1

ans = 0
for i in range(2, n + 1):
    if c[i] >= k:
        ans += 1
print(ans)