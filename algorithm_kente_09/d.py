n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
l = [(-(al[i] + bl[i]), -al[i], i + 1) for i in range(n)]
l.sort()
print(*[e[2] for e in l])
