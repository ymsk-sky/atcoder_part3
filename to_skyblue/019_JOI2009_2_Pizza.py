from bisect import bisect_left

d = int(input())
n = int(input())
m = int(input())
dl = [int(input()) for _ in range(n - 1)]
kl = [int(input()) for _ in range(m)]

dl = [0] + dl
bl = [d - b for b in dl]
bl[0] = 0

dl.sort()
bl.sort()

ans = 0
for k in kl:  # O(10**4)
    ix = bisect_left(dl, k)
    a1 = abs(k - dl[(ix - 1) % n])
    a2 = abs(k - dl[ix % n])
    a3 = abs(k - dl[(ix + 1) % n])

    l = d - k
    iy = bisect_left(bl, l)
    b1 = abs(l - bl[(iy - 1) % n])
    b2 = abs(l - bl[iy % n])
    b3 = abs(l - bl[(iy + 1) % n])

    tmp = min(a1, a2, a3, b1, b2, b3)
    ans += tmp

print(ans)