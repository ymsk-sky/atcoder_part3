r, g, b, n = map(int, input().split())
ans = 0
for i in range(3001):
    for j in range(3001):
        tmp = r*i + g*j
        rem = n - tmp
        if rem >= 0 and rem%b == 0:
            ans += 1
print(ans)
