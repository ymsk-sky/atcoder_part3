h, w, n = map(int, input().split())
"""
1つのマスあたり影響は9回しかない
-> O(9*n)
"""
s = set()
for _ in range(n):
    a, b = map(int, input().split())
    s.add((a, b))
ans = [0] * 10

"""
0.. .1. ..2 ... ... ... ... ... ...
... ... ... 3.. .4. ..5 ... ... ...
... ... ... ... ... ... 6.. .7. ..8
"""
rs = (((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)),
      ((0, -1), (0, 0),  (0, 1), (1, -1), (1, 0), (1, 1), (2, -1), (2, 0), (2, 1)),
      ((0, -2), (0, -1), (0, 0), (1, -2), (1, -1), (1, 0), (2, -2), (2, -1), (2, 0)),
      ((-1, 0), (-1, 1), (-1, 2), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)),
      ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)),
      ((-1, -2), (-1, -1), (-1, 0), (0, -2), (0, -1), (0, 0), (1, -2), (1, -1), (1, 0)),
      ((-2, 0), (-2, 1), (-2, 2), (-1, 0), (-1, 1), (-1, 2), (0, 0), (0, 1), (0, 2)),
      ((-2, -1), (-2, 0), (-2, 1), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1)),
      ((-2, -2), (-2, -1), (-2, 0), (-1, -2), (-1, -1), (-1, 0), (0, -2), (0, -1), (0, 0)))
for a, b in s:
    for r in rs:
        cnt = 0
        for k in range(9):
            i, j = r[k][0], r[k][1]
            u, v = a + i, b + j
            if 1 <= u <= h and 1 <= v <= w:
                if (u, v) in s:
                    cnt += 1
            else:
                break
        else:
            ans[cnt] += 1

for i in range(1, 10):
    ans[i] //= i
ans[0] = (h - 2)*(w - 2) - sum(ans)
print(*ans, sep="\n")