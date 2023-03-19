n, k = map(int, input().split())
al = list(map(int, input().split()))
ac = [0] * (n + 1)
for i in range(n):
    ac[i + 1] = ac[i] + al[i]
for x in range(n - k + 1):
    print(ac[x + k] - ac[x])
