n = int(input())
cl = list(map(int, input().split()))
q = int(input())

on = -(-n//2)
if n == 1:
    ans = 0
    for _ in range(q):
        s = list(map(int, input().split()))
        a = s[-1]
        if cl[0] >= a:
            cl[0] -= a
            ans += a
    print(ans)
    exit()

ml = [min([cl[i] for i in range(n) if i%2 == 1]),
      min([cl[i] for i in range(n) if i%2 == 0])]
ol = [0, 0]

ans = 0
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x, a = s[1:]
        mod = x%2
        if cl[x - 1] - ol[mod] >= a:
            cl[x - 1] -= a
            ans += a
            ml[mod] = min(ml[mod], cl[x - 1])
    elif s[0] == 2:
        a = s[1]
        if ml[1] - ol[1] >= a:
            ol[1] += a
            ans += a*on
    else:
        a = s[1]
        if ml[0] - ol[0] >= a and ml[1] - ol[1] >= a:
            ol[0] += a
            ol[1] += a
            ans += a*n
print(ans)
