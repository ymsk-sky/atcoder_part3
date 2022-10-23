n = int(input())
sl = list(map(int, input().split()))
l = set()
for a in range(1, 334):
    for b in range(1, 334):
        s = 4 * a * b + 3 * a + 3 * b
        l.add(s)

ans = 0
for s in sl:
    if not s in l:
        ans += 1
print(ans)