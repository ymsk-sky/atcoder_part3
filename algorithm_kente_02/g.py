from collections import deque

q = int(input())
que = deque()
ans = []
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        c = query[1]
        x = int(query[2])
        que.append((c, x))
    else:
        d = int(query[1])
        l = [0] * 26
        while que:
            c, x = que.popleft()
            if d > x:
                d -= x
                l[ord(c) - 97] += x
            else:
                x -= d
                l[ord(c) - 97] += d
                if x != 0:
                    que.appendleft((c, x))
                break
        ans.append(sum([d**2 for d in l]))

print(*ans, sep="\n")
