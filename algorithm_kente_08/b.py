n, m = map(int, input().split())
al = set(map(int, input().split()))
bl = set(map(int, input().split()))
print(*sorted(al & bl))
