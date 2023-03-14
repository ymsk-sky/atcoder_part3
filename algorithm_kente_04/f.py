from collections import Counter

n, k = map(int, input().split())
sl = [input() for _ in range(n)]
c = Counter(sl)
ans = sorted(c, key=lambda k: c[k], reverse=True)[k - 1]

for key in c:
    if c[key] == c[ans] and key != ans:
        print("AMBIGUOUS")
        break
else:
    print(ans)
