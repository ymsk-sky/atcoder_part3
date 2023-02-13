from itertools import product
n = int(input())
al = list(map(int, input().split()))
al = [(a - 1, a, a + 1) for a in al]
ans = 0
for pro in product(*al):
    s = 1
    for v in pro:
        s *= v
    if s%2 == 0:
        ans += 1
print(ans)
