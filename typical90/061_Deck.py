from collections import deque

q = int(input())
l = [list(map(int, input().split())) for _ in range(q)]

que = deque()
for t, x in l:
    if t == 1:
        # 上にxを追加
        que.appendleft(x)
    elif t == 2:
        # 下にxを追加
        que.append(x)
    elif t == 3:
        # 上からx番目を出力
        print(que[x - 1])