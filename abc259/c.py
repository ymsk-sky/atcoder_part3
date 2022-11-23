s = input()
t = input()
sl = []
bef = s[0]
cnt = 1
for c in s[1:]:
    if c == bef:
        cnt += 1
    else:
        sl.append((bef, cnt))
        cnt = 1
    bef = c
sl.append((bef, cnt))
tl = []
bef = t[0]
cnt = 1
for c in t[1:]:
    if c == bef:
        cnt += 1
    else:
        tl.append((bef, cnt))
        cnt = 1
    bef = c
tl.append((bef, cnt))

if len(sl) != len(tl):
    print("No")
else:
    for i in range(len(sl)):
        c1, n1 = sl[i]
        c2, n2 = tl[i]
        if c1 == c2:
            if n1 == n2:
                continue
            elif n1 > n2:
                print("No")
                exit()
            elif n1 < n2:
                if n1 == 1:
                    print("No")
                    exit()
        else:
            print("No")
            exit()
    print("Yes")