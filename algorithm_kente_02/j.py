s = input()
n = len(s)
tmp = [[] for _ in range(500)]
p = 0
for i in range(n):
    c = s[i]
    if c == "(":
        p += 1
    elif c == ")":
        t = "".join(tmp[p])
        tmp[p] = []
        p -= 1
        tmp[p].append(t + t[::-1])
    else:
        tmp[p].append(c)
print(*tmp[0], sep="")

"""
(ab)c
abbac
"""
