n = int(input())
hsl = [list(map(int, input().split())) for _ in range(n)]

left = 1
right = max([h + s * (n - 1) for h, s in hsl])
while right - left > 1:
    mid = (left + right) // 2
    pos = [0] * n
    for h, s in hsl:
        if mid < h:
            # そもそもmidが小さいと0秒でも達成不可のため大きな適当な値で埋める
            pos[0] += 9
            break
        # i秒以下であればmid以下の点数でいける
        i = min(max(0, (mid - h) // s), n - 1)
        pos[i] += 1
    f = True
    # pos[i - 1]番目まででi個以下であれば達成可能
    for i in range(1, n):
        if i >= pos[i - 1]:
            pos[i] += pos[i - 1]
        else:
            # (例)5秒以内に7個落とさないとmid(点)以下とならない -> 達成不可
            f = False
            break
    if f:
        # mid以下で達成可能
        right = mid
    else:
        # midより大きい値でないと達成不可
        left = mid
print(right)