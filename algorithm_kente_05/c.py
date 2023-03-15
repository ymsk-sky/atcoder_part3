n = int(input())
ans = []
l = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = n//36**2
if a != 0 or ans:
    ans.append(l[a])
n%=36**2
a = n//36**1
if a != 0 or ans:
    ans.append(l[a])
n%=36**1
a = n//36**0
ans.append(l[a])
print(*ans, sep="")
