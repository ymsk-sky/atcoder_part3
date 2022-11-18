h, w = map(int, input().split())
g = [input() for _ in range(h)]
visited = [[0] * w for _ in range(h)]
i, j = 0, 0
while 1:
    visited[i][j] = 1
    p = g[i][j]
    if p == "U":
        i -= 1
    elif p == "D":
        i += 1
    elif p == "R":
        j += 1
    elif p == "L":
        j -= 1
    if i < 0 or i >= h or j < 0 or j >= w:
        if p == "U":
            i += 1
        elif p == "D":
            i -= 1
        elif p == "R":
            j -= 1
        elif p == "L":
            j += 1
        break
    if visited[i][j]:
        print(-1)
        exit()
print(i + 1, j + 1)