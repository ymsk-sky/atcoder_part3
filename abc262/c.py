n = int(input())
al = list(map(int, input().split()))
same = [1 if al[i - 1] == i else 0 for i in range(1, n + 1)]
for i in range(n - 1):
    same[i + 1] += same[i]
ans = 0
for i in range(1, n):
    if al[i - 1] == i:
        ans += same[-1] - same[i - 1]
    elif al[i - 1] > i:
        j = al[i - 1]
        if al[j - 1] == i:
            ans += 1
print(ans)