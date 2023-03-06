n = int(input())
cl = list(map(int, input().split()))
q = int(input())
m = -(-n//2)  # 奇数番目の個数
# 最小値(閾値を考慮した実際の値)
min_all = 0
min_odd = 0
# 閾値
th_all = 0
th_odd = 0
ans = 0
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x, a = s[1:]
        if x%2 == 0:
            if cl[x - 1] - th_all >= a:
                cl[x - 1] -= a
                ans += a
                min_all = min(min_all, cl[x - 1] - th_all)
        else:
            th = th_all + th_odd
            if cl[x - 1] - th >= a:
                cl[x - 1] -= a
                ans += a
                min_all = min(min_all, cl[x - 1] - th)
                min_odd = min(min_odd, cl[x - 1] - th)
    elif s[0] == 2:
        a = s[1]
        if min_odd >= a:
            min_odd -= a
            min_all = min(min_all, min_odd)
            th_odd += a
            ans += a*m
    else:
        a = s[1]
        if min_all >= a:
            min_all -= a
            th_all += a
            ans += a*n

print(ans)
