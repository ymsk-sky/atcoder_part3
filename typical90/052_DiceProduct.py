n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
mod = 10 ** 9 + 7

s = [sum(a) for a in l]
ans = 1
for a in s:
    ans *= a
    ans %= mod
print(ans)