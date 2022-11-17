l = [list(map(int, input().split())) for _ in range(4)]

def vec(a, b):
    return [a[0] - b[0], a[1] - b[1]]
def in_triangle(a, b, c, p):
    ab = vec(b, a)
    bp = vec(p, b)

    bc = vec(c, b)
    cp = vec(p, c)

    ca = vec(a, c)
    ap = vec(p, a)

    c1 = ab[0]*bp[1] - ab[1]*bp[0]
    c2 = bc[0]*cp[1] - bc[1]*cp[0]
    c3 = ca[0]*ap[1] - ca[1]*ap[0]

    return (c1 > 0 and c2 > 0 and c3 > 0) or (c1 < 0 and c2 < 0 and c3 < 0)

for i in range(4):
    if in_triangle(l[i], l[(i+1) % 4], l[(i+2) % 4], l[(i+3) % 4]):
        print("No")
        exit()
print("Yes")