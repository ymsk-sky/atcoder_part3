"""
残りN回のときの期待値の最大値をf(N)と置くと
次で出目がDとすると,スコアは終了でD,続行でf(N-1)の大きいほうとなる
よって
f(N) = max(1,f(N-1))/6 + max(2,f(N-1))/6 + max(3,f(N-1))/6
       + max(4,f(N-1))/6 + max(5,f(N-1))/6 + max(6,f(N-1))/6
f(N)を小さいほうから(N=0)から順に計算すれば解ける
"""
n = int(input())
fl = [-1] * n
fl[0] = 3.5  # (1+2+3+4+5+6)/6
for i in range(1, n):
    f = fl[i - 1]
    ans = (max(1, f) + max(2, f) + max(3, f)
           + max(4, f) + max(5, f) + max(6, f)) / 6
    fl[i] = ans
print(fl[n - 1])