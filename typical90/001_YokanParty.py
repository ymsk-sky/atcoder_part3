"""答えで二分探索
答えは1~LなのでO(logL)
「答えはM以上か?」 -> 「(K+1)個以上の, 長さM以上のピースに分割可能か?」
次に「最大何個の, 長さM以上のピースに分割できるか?」という判定問題を考える
-> 左から見ていき, 「はじめてM以上になったところで切る」を繰り返して確認(O(N))

よってO(NlogL)で回答可能
"""

n, l = map(int, input().split())
k = int(input())
al = [0] + list(map(int, input().split())) + [l]
al = [b - a for a, b in zip(al, al[1:])]  # ピースの長さの数列にする
left = 1
right = l
while right - left > 1:
    mid = (left + right) // 2  # mid = M
    cnt = 0  # 切れ目の数
    b = 0  # 蓄積された長さ
    for a in al:
        b += a
        if b >= mid:
            cnt += 1
            b = 0
    if b == 0:  # 最後がmid以上
        cnt -= 1
        if cnt >= k:
            left = mid
        else:
            right = mid
    else:
        if cnt > k:
            # 切れ目が(k + 1)個以上なら最後のピースはひとつ前に入れてしまうので問題ない
            left = mid
        else:
            right = mid
print(left)

"""
1<=k<=10**5
0<a1<a2<...<an<l<=10**9
"""
