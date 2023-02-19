n = int(input())
dl = list(map(int, input().split()))
m = int(input())
tl = list(map(int, input().split()))

if n < m:
    print("NO")
    exit()

dl.sort()
tl.sort()
cnt = 0
i = 0
for j in range(m):
    t = tl[j]
    while i < n:
        d = dl[i]
        if t == d:
            cnt += 1
            i += 1
            break
        i += 1
print("YES" if cnt == m else "NO")
