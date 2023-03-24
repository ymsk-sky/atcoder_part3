n = int(input())
ans = 0
cl = (500, 100, 50, 10, 5, 1)
o = {50, 5}
for _ in range(n):
    a, b = map(int, input().split())
    m = b - a
    for c in cl:
        if c in o:
            ans += m//c
        m %= c
print(ans)
