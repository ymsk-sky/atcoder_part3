from math import gcd
def fin():
    print(-1)
    exit()

n, m = map(int, input().split())
s = input()
t = input()

l = n*m//gcd(n, m)
d = dict()
d[0] = s[0]
for i in range(1, n):
    d[l//n*i] = s[i]
if d[0] != t[0]:
    fin()
for i in range(1, m):
    j = l//m*i
    if j in d:
        if d[j] != t[i]:
            fin()
print(l)
