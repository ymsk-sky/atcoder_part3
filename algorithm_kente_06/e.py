from collections import deque

n = int(input())
s = input()
ERR = "ERROR"
que = deque()
ans = []
for i in range(1, n + 1):
    c = s[i - 1]
    if c == "L":
        que.appendleft(i)
    elif c == "R":
        que.append(i)
    elif c == "A":
        if que:
            ans.append(que.popleft())
        else:
            ans.append(ERR)
    elif c == "B":
        if len(que) > 1:
            tmp = que.popleft()
            ans.append(que.popleft())
            que.appendleft(tmp)
        else:
            ans.append(ERR)
    elif c == "C":
        if len(que) > 2:
            tmp1 = que.popleft()
            tmp2 = que.popleft()
            ans.append(que.popleft())
            que.appendleft(tmp2)
            que.appendleft(tmp1)
        else:
            ans.append(ERR)
    elif c == "D":
        if que:
            ans.append(que.pop())
        else:
            ans.append(ERR)
    elif c == "E":
        if len(que) > 1:
            tmp = que.pop()
            ans.append(que.pop())
            que.append(tmp)
        else:
            ans.append(ERR)
    elif c == "F":
        if len(que) > 2:
            tmp1 = que.pop()
            tmp2 = que.pop()
            ans.append(que.pop())
            que.append(tmp2)
            que.append(tmp1)
        else:
            ans.append(ERR)
print(*ans, sep="\n")
