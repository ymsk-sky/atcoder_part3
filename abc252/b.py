n, k = map(int, input().split())
al = list(map(int, input().split()))
bl = set(map(int, input().split()))
m = max(al)
for i in range(1, n + 1):
    if al[i - 1] == m:
        if i in bl:
            print("Yes")
            exit()
print("No")