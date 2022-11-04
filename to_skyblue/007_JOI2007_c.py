from sys import stdin
from itertools import permutations

def solve():
    n = int(stdin.readline())
    xyl = {tuple(map(int, stdin.readline().split())) for _ in range(n)}

    ans = 0
    for (x1, y1), (x2, y2) in permutations(xyl, 2):
        if x1 < x2 and x1 <= y2:
            dx = y2 - y1
            dy = x2 - x1

            x3, y3 = x2 + dx, y2 - dy
            x4, y4 = x3 - dy, y3 - dx

            if (x3, y3) in xyl and (x4, y4) in xyl:
                ans = max(ans, dx ** 2 + dy ** 2)
    print(ans)

solve()