n = input()
l = set("12345")
r = set("67890")
ans = 500
bef = n[0]
for crt in n[1:]:
    if crt == bef:
        ans += 301
    elif len({crt, bef} & l) == 2 or len({crt, bef} & r) == 2:
        ans += 210
    else:
        ans += 100
    bef = crt
print(ans)
