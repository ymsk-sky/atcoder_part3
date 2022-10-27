k = int(input())
ans = 0
for a in range(1, k + 1):
    if a * a * a > k:
        break
    for b in range(a, k + 1):
        if a * b * b > k:
            break
        ab = a * b
        if k % ab == 0 and k // ab >= b:
            ans += 1
print(ans)