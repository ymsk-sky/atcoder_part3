n, k = map(int, input().split())

def t810(v):
    s = str(v)[::-1]
    l = len(s)
    return sum([int(s[i]) * 8 ** i for i in range(l)])

def t109(v):
    tmp = []
    while v >= 9:
        tmp.append(v % 9)
        v //= 9
    tmp.append(v)
    return tmp

ans = n
for _ in range(k):
    # 8->10
    n10 = t810(ans)
    # 10->9
    n9 = t109(n10)
    # "8"->"5"
    l = len(n9)
    ans = sum([5 * 10 ** i if n9[i] == 8 else n9[i] * 10 ** i for i in range(l)])

print(ans)