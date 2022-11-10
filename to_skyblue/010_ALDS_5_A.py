from itertools import combinations

n = int(input())
al = list(map(int, input().split()))
q = int(input())
ml = list(map(int, input().split()))

l = [0] * 2001
for i in range(1, n + 1):
    for comb in combinations(al, i):
        l[sum(comb)] = 1

for m in ml:
    print("yes" if l[m] else "no")