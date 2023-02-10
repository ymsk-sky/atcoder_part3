q, h, s, d = map(int, input().split())
n = int(input())
# 2Lあたりの値段にする
a, b, c, d = 8*q, 4*h, 2*s, d
l = sorted([[a, q, 1/4], [b, h, 1/2], [c, s, 1], [d, d, 2]])

ans = 0
for _, val, qua in l:
    ans += int(n//qua * val)
    n %= qua
print(ans)
