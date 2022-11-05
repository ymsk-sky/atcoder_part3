r, c = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(r)]
ans = r * c
for i in range(1 << r):
    state = [(i >> j) & 1 for j in range(r)]
    tmp = 0
    for j in range(c):
        o, x = 0, 0
        for k in range(r):
            if state[k] ^ s[k][j]:
                o += 1
            else:
                x += 1
        tmp += min(o, x)

    ans = min(ans, tmp)
    if ans == 2:
        print(i)
print(r * c - ans)