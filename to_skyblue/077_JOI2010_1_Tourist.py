n, m = map(int, input().split())
sl = [int(input()) for _ in range(n - 1)]
al = [int(input()) for _ in range(m)]
mod = 10 ** 5

wl = [0] * (n + 1)
for i in range(1, n):
    wl[i + 1] = wl[i] + sl[i - 1]

ans = 0

crt = 1
for a in al:
    nxt = crt + a
    d = abs(wl[nxt] - wl[crt])
    ans += d
    ans %= mod
    crt = nxt

print(ans)