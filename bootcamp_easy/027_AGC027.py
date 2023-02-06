n, x = map(int, input().split())
al = list(map(int, input().split()))
al.sort()
ans = 0
for i in range(n):
    a = al[i]
    if a <= x:
        if i == n - 1:
            if a < x:
                continue
        x -= a
        ans += 1
print(ans)
