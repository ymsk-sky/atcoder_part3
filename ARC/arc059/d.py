s = input()
n = len(s)
# 連続3個しか見る必要ない
if n < 3:
    if len(set(s)) == 1:
        print(1, n)
    else:
        print(-1, -1)
    exit()

for i in range(1, n - 1):
    a, b, c = s[i - 1], s[i], s[i + 1]
    if a == b or b == c or c == a:
        print(i, i + 2)
        exit()
print(-1, -1)