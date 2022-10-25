"""
期待値の線形性:
    X1の期待値 + X2の期待値 + ... Xnの期待値 = (X1+X2+...+Xn)の期待値
"""
n = int(input())
lrl = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    l1, r1 = lrl[i]
    for j in range(i + 1, n):
        l2, r2 = lrl[j]
        al, cnt = 0, 0
        for a in range(l1, r1 + 1):
            for b in range(l2, r2 + 1):
                al += 1
                if a > b:
                    cnt += 1
        ans += cnt / al
print(ans)