from collections import deque

n = int(input())
cl = [int(input()) for _ in range(n)]

q = deque()
for i in range(n):
    c = cl[i]
    if i % 2 == 0:
        # 奇数番目
        if q:
            bef, num = q.pop()
            if bef == c:
                q.append([bef, num + 1])
            else:
                q.append([bef, num])
                q.append([c, 1])
        else:
            q.append([c, 1])
    else:
        # 偶数番目
        bef, num = q.pop()
        if bef == c:
            q.append([bef, num + 1])
        else:
            if q:
                b_bef, b_num = q.pop()
                q.append([c, b_num + num + 1])
            else:
                q.append([c, num + 1])
ans = 0
while q:
    c, num = q.pop()
    if c == 0:
        ans += num
print(ans)