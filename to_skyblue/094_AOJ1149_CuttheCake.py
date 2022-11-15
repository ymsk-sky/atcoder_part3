from collections import deque

ans = []
while 1:
    # n: 切る回数, w: 幅, d: 高さ
    n, w, d = map(int, input().split())
    if w == 0 and d == 0:
        break
    psl = [list(map(int, input().split())) for _ in range(n)]
    q = deque([(w, d)])  # 番号順
    tmp = deque()  # 番号順
    for p, s in psl:
        # (p-1)番目までを一旦取り出す
        for _ in range(p - 1):
            tmp.append(q.popleft())
        # p番目をs位置で切る
        w, d = q.popleft()
        w1 = w2 = w
        d1 = d2 = d
        m = s % (2 * w + 2 * d)
        if 0 < m <= w:
            w1, w2 = m, w - m
        elif w < m <= w + d:
            m -= w
            d1, d2 = m, d - m
        elif w + d < m <= 2 * w + d:
            m -= w + d
            w1, w2 = m, w - m
        else:
            if m == 0:
                m = 2 * w + 2 * d
            m -= 2 * w + d
            d1, d2 = m, d - m
        for _ in range(p - 1):
            q.appendleft(tmp.pop())
        if w1 * d1 > w2 * d2:
            w1, d1, w2, d2 = w2, d2, w1, d1
        q.append((w1, d1))
        q.append((w2, d2))
    res = []
    while q:
        w, d = q.pop()
        res.append(w * d)
    ans.append(sorted(res))
for an in ans:
    print(*an)