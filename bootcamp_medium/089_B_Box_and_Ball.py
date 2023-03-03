n, m = map(int, input().split())
# 赤, 白
box = [[0, 1] for _ in range(n)]
box[0] = [1, 0]
for _ in range(m):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    if box[x][0]:
        # 赤の移動の可能性
        if box[x][1]:
            pass
        else:
            # 赤が移動するしかない
            pass
    else:
        # 移動は白のみ
        pass
