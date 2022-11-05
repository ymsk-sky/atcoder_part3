n, m = map(int, input().split())
kl = []
sll = []
for _ in range(m):
    k, *sl = list(map(int, input().split()))
    kl.append(k)
    sll.append(sl)
pl = list(map(int, input().split()))

ans = 0
for b in range(1 << n):
    state = [(b >> i) & 1 for i in range(n)]
    for i in range(m):
        sl = sll[i]
        cnt = 0
        for s in sl:
            if state[s - 1]:
                cnt += 1
        if cnt % 2 != pl[i]:
            break
    else:
        ans += 1
print(ans)