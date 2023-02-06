a, b, c = map(int, input().split())
ans = 0

while a%2 == 0 and b%2 == 0 and c%2 == 0:
    if a == b == c:
        print(-1)
        exit()
    a2, b2, c2 = a//2, b//2, c//2
    a, b, c = b2 + c2, a2 + c2, a2 + b2
    ans += 1
print(ans)
