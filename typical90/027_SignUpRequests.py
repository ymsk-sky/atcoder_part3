n = int(input())
sl = [input() for _ in range(n)]
reg = set()
for i in range(n):
    s = sl[i]
    if s in reg:
        continue
    else:
        reg.add(s)
        print(i + 1)