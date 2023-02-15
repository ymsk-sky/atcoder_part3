from itertools import permutations

n = int(input())
pl = list(map(int, input().split()))
ql = list(map(int, input().split()))

for i, per in enumerate(permutations(range(1, n + 1)), start=1):
    per = list(per)
    if pl == per:
        a = i
    if ql == per:
        b = i
print(abs(a - b))

