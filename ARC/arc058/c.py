n, k = map(int, input().split())
dl = set(map(int, input().split()))

for i in range(n, 10**6):
    s = set([int(c) for c in str(i)])
    if len(s & dl) == 0:
        print(i)
        exit()