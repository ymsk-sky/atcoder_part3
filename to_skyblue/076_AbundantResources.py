n = int(input())
al = list(map(int, input().split()))
wl = [0] * (n + 1)
for i in range(n):
    wl[i + 1] += wl[i] + al[i]
for k in range(1, n + 1):
    ans = 0
    for i in range(n):
        if i + k > n:
            break
        tmp = wl[i + k] - wl[i]
        ans = max(ans, tmp)
    print(ans)
