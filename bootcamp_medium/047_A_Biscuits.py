from math import factorial as f

def cnt(n, k):
    return f(n)//(f(n - k)*f(k))

n, p = map(int, input().split())
al = list(map(int, input().split()))
odd = 0
even = 0
for a in al:
    if a%2 == 0:
        even += 1
    else:
        odd += 1

ans = sum([cnt(even, i) for i in range(even + 1)])
if p == 0:
    ans *= sum([cnt(odd, i) for i in range(0, odd + 1, 2)])
else:
    ans *= sum([cnt(odd, i) for i in range(1, odd + 1, 2)])
print(ans)
