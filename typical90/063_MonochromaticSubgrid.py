from collections import Counter

h, w = map(int, input().split())
pl = [list(map(int, input().split())) for _ in range(h)]

popcount = [bin(i).count("1") for i in range(2 ** h)]

ans = 0
for k in range(1, 2 ** h):
    cnt = popcount[k]
    l = [pl[i] for i in range(h) if (k >> i) & 1]
    l = [z[0] for z in zip(*l) if len(set(z)) == 1]
    c = Counter(l)
    if len(c) > 0:
        tmp = c.most_common()[0][1] * cnt
        ans = max(ans, tmp)
print(ans)