s = input()
n = len(s) + 1

bef = s[0]
cnt = 1
l = []
for c in s[1:]:
    if bef == c:
        cnt += 1
    else:
        l.append((cnt, bef))
        bef = c
        cnt = 1
l.append((cnt, bef))

ans = 0
head = 0
for num, ch in l:
    if ch == "<":
        # head ~ (head + num) の和
        a = head
        b = head + num
        ans += (a + b)*(b - a + 1)//2
        head = b
    else:
        # 0 ~ num の和 = tmp
        tmp = num*(num + 1)//2
        if head >= num:  # ただしhead >= numのとき tmp -= num
            tmp -= num
        else:  # もしくはhead < numのとき tmp += num - head
            tmp -= head
        ans += tmp
        head = 0
print(ans)

"""
 < > > > < < > < < < < < > > > <
0 3 2 1 0 1 2 0 1 2 3 4 5 2 1 0 1

1 3 2 1 5 3 1
< > < > < > <

0 3 2 1 0
ans = 1
head = 1
num = 3
tmp = 6
"""
