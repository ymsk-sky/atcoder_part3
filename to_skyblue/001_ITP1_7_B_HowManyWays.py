while 1:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    ans = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if a + b + c == x:
                    ans += 1
    print(ans)
