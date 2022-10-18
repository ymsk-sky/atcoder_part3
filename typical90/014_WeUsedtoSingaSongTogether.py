n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

al.sort()
bl.sort()
ans = sum([abs(a - b) for a, b in zip(al, bl)])
print(ans)