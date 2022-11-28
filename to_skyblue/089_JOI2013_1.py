n = int(input())
al = list(map(int, input().split()))
"""
交互列の塊ごとに長さを求めて
ある交互列xを反転させると (x-1), x, (x+1)の交互列が繋がるためそれを最大にする
"""
l = []
bef = al[0]
cnt = 1
for a in al[1:]:
    if bef != a:
        cnt += 1
    else:
        l.append(cnt)
        cnt = 1
    bef = a
l.append(cnt)
l.append(0)
l.append(0)

ans = 0
for i in range(len(l) - 2):
    s = l[i] + l[i + 1] + l[i + 2]
    ans = max(ans, s)
print(ans)