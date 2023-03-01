t = list(input())
s = t[:]
k = int(input())
n = len(s)

if len(set(s)) == 1:
    print(n*k//2)
    exit()

ans = 0
for i in range(1, n):
    if s[i - 1] == s[i]:
        ans += 1
        s[i] = "#"
ans *= k

s = t[:]
if s[0] == s[-1]:
    i = 1
    while s[i] == s[0]:
        i += 1
    a = i
    j = -2
    while s[j] == s[-1]:
        j -= 1
    b = -j -1
    ans -= (a//2 + b//2 - (a + b)//2)*(k - 1)

print(ans)
