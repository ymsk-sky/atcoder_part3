while 1:
    n = int(input())
    if n == 0:
        break
    l = [0] * 240002
    for _ in range(n):
        st, ed = map(lambda x: int("".join(x.split(":"))), input().split())
        l[st] += 1
        l[ed] -= 1
    for i in range(240001):
        l[i + 1] += l[i]
    print(max(l))