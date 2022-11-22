n, k, q = map(int, input().split())
al = list(map(int, input().split()))
ll = list(map(int, input().split()))
for l in ll:
    a = al[l - 1]
    if l == k:
        if a != n:
            al[l - 1] += 1
    else:
        b = al[l]
        if a + 1 != b:
            al[l - 1] += 1
print(*al)