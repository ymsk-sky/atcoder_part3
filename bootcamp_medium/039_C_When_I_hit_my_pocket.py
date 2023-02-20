k, a, b = map(int, input().split())
if a + 1 < b:
    tmp1 = k//(a + 2)*b  # 交換
    tmp2 = k%(a + 2) + 1  # 残り
    print(tmp1 + tmp2)
else:
    print(k + 1)
