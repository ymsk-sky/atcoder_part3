n, m = map(int, input().split())
al = [set(list(map(int, input().split()))[1:]) for _ in range(n)]
p, q = map(int, input().split())
bl = set(map(int, input().split()))
ans = 0
for a in al:
    if len(a & bl) >= q:
        ans += 1
print(ans)
