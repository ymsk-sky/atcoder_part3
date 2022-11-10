from itertools import permutations

k = int(input())
ans = [-1] * 8
for _ in range(k):
    r, c = map(int, input().split())
    ans[r] = c

for per in permutations(range(8)):
    cnt = 0
    for i in range(8):
        if ans[i] >= 0:
            if per[i] == ans[i]:
                cnt += 1
    if cnt != k:
        continue
    for i in range(8):
        j = per[i]
        f = True
        for u, v in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            y, x = i, j
            while 1:
                y += u
                x += v
                if 0 > y or y > 7 or 0 > x or x > 7:
                    break
                if per[y] == x:
                    f = False
                    break
            if not f:
                break
        if not f:
            break
    if f:
        break

for p in per:
    line = ["."] * 8
    line[p] = "Q"
    print(*line, sep="")