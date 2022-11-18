s = input()
t = "atcoder"

s = [t.index(c) for c in s]

cnt = 0
for i in range(7):
    if s[i] == i:
        continue
    j = s.index(i)
    for k in range(j - i):
        s[j - k], s[j - 1 - k] = s[j - 1 - k], s[j - k]
        cnt += 1
print(cnt)