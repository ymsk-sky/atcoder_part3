ans = []
while 1:
    h = int(input())
    if h == 0:
        break
    l = [list(map(int, input().split())) for _ in range(h)]
    res = 0
    while 1:
        # 得点処理(加点 + 消滅)
        point = 0
        for i in range(h):
            bef = l[i][0]
            cnt = 1
            w = []
            for j in range(1, 5):
                if l[i][j] == bef:
                    cnt += 1
                else:
                    w.append([bef, cnt])
                    cnt = 1
                bef = l[i][j]
            w.append([bef, cnt])
            for num, cnt in w:
                if cnt > 2:
                    point += num * cnt
            l[i] = [num if cnt < 3 else 0 for num, cnt in w for _ in range(cnt)]
        if point == 0:
            break
        res += point
        # 落下処理
        for j in range(5):
            t = [l[i][j] for i in range(h) if l[i][j] != 0]
            t = [0] * (h - len(t)) + t
            for i in range(h):
                l[i][j] = t[i]
    ans.append(res)
print(*ans, sep="\n")