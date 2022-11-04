from sys import stdin

def solve():
    n = int(stdin.readline())
    al = []
    bl = []
    for _ in [0] * n:
        a, b = map(int, stdin.readline().split())
        al.append(a)
        bl.append(b)
    al.sort()
    bl.sort()

    st = al[n // 2]
    go = bl[n // 2]

    ans = 0
    for a, b in zip(al, bl):
        d = abs(a - st) + (b - a) + abs(go - b)
        ans += d
    print(ans)

solve()