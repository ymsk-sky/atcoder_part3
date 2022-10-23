n, k, a = map(int, input().split())
l = [i for i in range(1, n + 1)] * 2
print(l[a - 1 + k % n - 1])
