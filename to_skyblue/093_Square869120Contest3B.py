import copy

h, w, K = map(int, input().split())
c = [list(map(int, input())) for _ in range(h)]

def solve(cc):
    score = []
    while 1:
        # drop
        keeped = True
        for j in range(w):
            l = [cc[i][j] for i in range(h)]
            m = [e for e in l if e != 0]
            m = [0] * (h - len(m)) + m
            if l != m:
                for i in range(h):
                    cc[i][j] = m[i]
                keeped = False
        if keeped:
            # 変動がない場合
            break
        # add_score
        crt_score = 0
        for i in range(h):
            l = []
            bef = -1
            cnt = 1
            for j in range(w):
                if cc[i][j] == bef:
                    cnt += 1
                else:
                    l.append((bef, cnt))
                    cnt = 1
                bef = cc[i][j]
            l.append((bef, cnt))
            for num, cnt in l:
                if cnt >= K:
                    crt_score += num * cnt
            cc[i] = [num if cnt < K else 0 for num, cnt in l for _ in range(cnt)][1:w + 1]
        if crt_score > 0:
            score.append(crt_score)
    return sum([2 ** i * score[i] for i in range(len(score))])

ans = 0
for i in range(h):
    for j in range(w):
        cc = copy.deepcopy(c)
        cc[i][j] = 0
        ans = max(ans, solve(cc))
print(ans)