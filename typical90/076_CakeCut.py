n = int(input())
al = list(map(int, input().split()))
s = sum(al)
if s / 10 != s // 10:
    print("No")
    exit()
s //= 10

# しゃくとり法を2周: 長さがsを超えた時点でleftをシフトするためrightがleftを追い越すことはない
length = 0
right = 0
for left in range(n * 2):
    while length + al[right % n] <= s:
        length += al[right % n]
        right += 1
    if length == s:
        print("Yes")
        exit()
    if left == right:
        right += 1
    else:
        length -= al[left % n]
print("No")