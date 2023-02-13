n = int(input())
al = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    a = al[i - 1]
    if i == al[a - 1]:
        ans += 1
print(ans//2)
