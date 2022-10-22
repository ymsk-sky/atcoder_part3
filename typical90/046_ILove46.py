from collections import Counter

n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))

al = [a % 46 for a in al]
bl = [b % 46 for b in bl]
cl = [c % 46 for c in cl]

ac = Counter(al)
bc = Counter(bl)
cc = Counter(cl)

ans = 0
for ak in ac:
    for bk in bc:
        for ck in cc:
            if (ak + bk + ck) % 46 == 0:
                s = ac[ak] * bc[bk] * cc[ck]
                ans += s
print(ans)