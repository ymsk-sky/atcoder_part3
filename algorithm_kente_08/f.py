from collections import deque

n = int(input())
s = input()
if s.count("0") == 1:
    print(-1)
    exit()

ans = [0] * n
que = deque()
for i in range(n):
    if s[i] == "1":
        ans[i] = i + 1
    else:
        que.append(i + 1)

que.rotate()
for i in range(n):
    if ans[i] == 0:
        ans[i] = que.popleft()

print(*ans)
