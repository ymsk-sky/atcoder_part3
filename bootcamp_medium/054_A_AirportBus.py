n, c, k = map(int, input().split())
tl = [int(input()) for _ in range(n)]
tl.sort()
ans = 0
cnt = 0
st = 0
for t in tl:
    if cnt == 0:
        st = t
        cnt = 1
        ans += 1
    else:
        if t - st <= k:
            if cnt < c:
                cnt += 1
            else:
                # 満員
                st = t
                cnt = 1
                ans += 1
        else:
            # 最初に乗る予定の人の限界
            st = t
            cnt = 1
            ans += 1
print(ans)
