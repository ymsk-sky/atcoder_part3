n = int(input())
al = list(map(int, input().split()))
l = list(range(2**n))
ans = [1] * 2**n
for k in range(2, n + 1):
    tmp = []
    for i, j in zip(l[::2], l[1::2]):
        if al[i] > al[j]:
            tmp.append(i)
        else:
            tmp.append(j)
    for i in tmp:
        ans[i] = k
    l = tmp[:]

print(*ans, sep="\n")
