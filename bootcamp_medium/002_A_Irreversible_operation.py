s = list(input())
n = len(s)
ans = 0
left = 0  # 左にたまったWの数
for i in range(n - 1):
    if s[i] == "B":
        if s[i + 1] == "W":
            ans += (i + 1) - left
            left += 1
            s[i + 1] = "B"
    else:
        # Wなので左にたまる
        left += 1
print(ans)

"""
一番左のBWから処理していく

BBW > BWB　> WBB : Wが左に貯まっていく
WBW > WWB >
"""
