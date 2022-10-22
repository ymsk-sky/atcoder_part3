n, q = map(int, input().split())
al = list(map(int, input().split()))
l = [list(map(int, input().split())) for _ in range(q)]
z = 0  # ずれ
for t, x, y in l:
    if t == 1:
        al[(x - 1 + z) % n], al[(y - 1 + z) % n] = al[(y - 1 + z) % n], al[(x - 1 + z) % n]
    elif t == 2:
        z -= 1
    else:
        print(al[(x - 1 + z) % n])