a, b, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
ans = min(al) + min(bl)
for _ in range(m):
    x, y, c = map(int, input().split())
    tmp = al[x - 1] + bl[y - 1] - c
    ans = min(ans, tmp)
print(ans)