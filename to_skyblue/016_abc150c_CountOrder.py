from itertools import permutations

n = int(input())
pl = tuple(map(int, input().split()))
ql = tuple(map(int, input().split()))

l = [i for i in range(1, n + 1)]
a = b = 0
for i, per in enumerate(permutations(l), start=1):
    if per == pl:
        a = i
    if per == ql:
        b = i
print(abs(a - b))