s = input()
n = len(s)
ans = 1
bef = s[0]
i = 1
while i < n:
    crt = s[i]
    if crt == bef:
        if i == n - 1:
            break
        bef = crt + s[i + 1]
        i += 1
    else:
        bef = crt
    i += 1
    ans += 1
print(ans)
