n = int(input())
ans = 0
for a in range(1, n + 1):
    # a<=b<=cよりb,cは最低aなのでa**3がnを超えていればb,cは存在しえない
    if a ** 3 > n:
        break
    for b in range(a, n + 1):
        # a<=b<=cよりcは最低bなのでa*b*bがnを超えていればcは存在しえない
        if a * b * b > n:
            break
        # cの上限値
        c_lim = n // a // b
        # cは(b ~ c_lim)の範囲の個数
        c_cnt = c_lim - b + 1
        ans += c_cnt
print(ans)

"""
1<=n<=10**11
"""