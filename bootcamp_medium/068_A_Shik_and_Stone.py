h, w = map(int, input().split())
a = [input() for _ in range(h)]
cnt = sum([l.count("#") for l in a])

def dfs(i, j, c):
    if 0 > i or i >= h or 0 > j or j >= w:
        return
    if a[i][j] == ".":
        return
    if i == h - 1 and j == w - 1:
        if c + 1 == cnt:
            print("Possible")
            exit()
    dfs(i + 1, j, c + 1)
    dfs(i, j + 1, c + 1)

dfs(0, 0, 0)
print("Impossible")
