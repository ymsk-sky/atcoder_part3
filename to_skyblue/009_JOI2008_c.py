from sys import stdin

def solve():
    m = int(stdin.readline())
    xyml = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
    n = int(stdin.readline())
    xynl = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

    xyml.sort()
    xynl.sort()

    xm, ym = xyml[0]
    for j in range(n - m + 1):
        xn, yn = xynl[j]
        dx, dy = xn - xm, yn - ym

        cnt = 1
        k = j + 1
        for i in range(1, m):
            xmi, ymi = xyml[i]
            while k < n:
                xnk, ynk = xynl[k]
                k += 1
                if xnk - xmi == dx and ynk - ymi == dy:
                    cnt += 1
                    break
        if cnt == m:
            print(dx, dy)
            return
solve()