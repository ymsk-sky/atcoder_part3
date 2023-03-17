n = int(input())
al = list(map(int, input().split()))
ans = []
for i in range(1, n + 1):
    x = i
    j = 0
    while 1:
        x = al[x - 1]
        j += 1
        if x == i:
            break
    ans.append(j)
print(*ans)
