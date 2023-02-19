n = int(input())
al = list(map(int, input().split()))
ans = 1
s = ""
bef = al[0]
for a in al[1:]:
    if s == "+":
        if bef > a:
            ans += 1
            s = ""
    elif s == "-":
        if bef < a:
            ans += 1
            s = ""
    else:
        if bef > a:
            s = "-"
        elif bef < a:
            s = "+"
    bef = a
print(ans)
